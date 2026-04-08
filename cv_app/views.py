from django.shortcuts import render, get_object_or_404  
from django.views.generic import View, ListView, DetailView
from cv_app.models import CV
# from openai import OpenAI
from cv_app.forms import CreateCVForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from google import genai
from dotenv import load_dotenv
import os



# Create your views here.

def check_user_limit(user):
    today = timezone.now().date()
 
    if user.is_premium:
        user.requests += 1
        user.save()
        return True
    else:
        if user.limit_date != today:
            user.requests = 0
            user.limit_date = today
    
        if user.requests >= user.limit_requests:
            return False
    user.requests += 1
    user.save()
    return True


class CreateCVView(View):
    model = CV
    template_name='create_cv.html'
    form_class = CreateCVForm


    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form":form})
    
    def post(self, request):
        # client = OpenAI()
        client = genai.Client()


        form = self.form_class(request.POST)
        if form.is_valid():

            if not check_user_limit(request.user):
                messages.error(request, "Kunlik limitingiz tugagan, foydalanishni davom ettirish uchun premium obuna kerak yoki ertagacha kuting!")
                return render(request, self.template_name, {"form":form})
            else:

                cv_info = form.save(commit=False)
                cv_info.author = request.user
            
                name = cv_info.ism
                surname = cv_info.familiya
                dob = cv_info.t_sana
                email = cv_info.email
                phone = cv_info.phone
                education = cv_info.education
                experience = cv_info.experience
                skills = cv_info.skills
                languages = cv_info.languages
                hobbies = cv_info.hobbies

                prompt = f"""
                    Siz 15 yillik tajribaga ega professional HR mutaxassisi va CV yozuvchi mutaxassissiz.
                    Foydalanuvchi bergan ma'lumotlar asosida zamonaviy, professional va ish beruvchilarni jalb qiladigan CV yarating.

                    Foydalanuvchi ma'lumotlari:

                    Ism: {name}
                    Familiya: {surname}
                    Tug'ilgan sana: {dob}
                    Email: {email}
                    Telefon: {phone}
                    Ta'lim: {education}
                    Ish tajribasi: {experience}
                    Ko'nikmalar: {skills}
                    Tillari: {languages}
                    Hobbi: {hobbies}

                    Talablar:

                    - Zamonaviy va professional CV yarating
                    - Qisqa ma'lumotlarni professional tarzda kengaytiring
                    - Professional uslubda yozing
                    - CV tartibli va chiroyli formatda bo'lsin
                    - Ish beruvchini qiziqtiradigan qilib yozing
                    - Professional "Summary" qo‘shing
                    - Tajriba bo‘limida mas'uliyat va yutuqlarni yozing
                    - Ko‘nikmalarni professional tarzda tartiblang
                    - CV rasmiy va professional ohangda bo‘lsin

                    Quyidagi strukturada yozing:

                    # {name} {surname}

                    ## Professional Xulosa
                    3-5 ta professional gap yozing

                    ## Aloqa ma'lumotlari
                    - Email: {email}
                    - Telefon: {phone}
                    - Tug'ilgan sana: {dob}

                    ## Ta'lim
                    Ta'limni professional tarzda kengaytirib yozing

                    ## Ish Tajribasi
                    Mas'uliyatlar va yutuqlar bilan yozing

                    ## Ko'nikmalar
                    Professional ko'nikmalarni tartibli yozing

                    ## Tillar
                    Bilish darajasi bilan yozing

                    ## Qo'shimcha ma'lumotlar
                    Professional qo‘shimcha ma'lumot qo‘shing

                    ## Hobbi
                    Hobbi va qiziqishlar

                    Natijani professional CV ko'rinishida qaytaring.
                    Faqat CV matnini qaytaring.
                    """
                try:
                    response = client.models.generate_content(
                        model="gemini-3-flash-preview",
                        contents=prompt,
                    )

                    # cv_info.cv_text = response.choices[0].message.content
                    cv_info.cv_text = response.text
                    cv_info.save()
                
                    return redirect('cv-detail', pk=cv_info.pk)

                except Exception as e:
                    print(e)
                    messages.error(request, f"Server band keyinroq urinib ko'ring!{e}")
                    return render(request, self.template_name, {"form":form})
        return render(request, self.template_name, {"form":form})
    
class UserCVListView(ListView):
    template_name = 'user_cv.html'
    context_object_name = 'cv'
    model = CV

    def get_queryset(self):
        return self.request.user.cv.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['today'] = timezone.now().date()

        return context

class UserCVDetailView(DetailView):
    model = CV
    template_name = 'cv_detail.html'
    context_object_name = 'cv'

    def get_object(self):
        return get_object_or_404(CV, pk=self.kwargs['pk'], author=self.request.user)