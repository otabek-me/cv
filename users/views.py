from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView, View
from users.forms import LoginForm, UserCreateForm, UserUpdateForm
from django.urls import reverse_lazy
from users.models import Users
from django.utils import timezone
from datetime import timedelta



class LoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request,"ok")      
        return super().form_valid(form)

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Muvafaqiyatli ro\'yxatdan o\'tildi')
        return super().form_valid(form)

class UserUpdateView(UpdateView):
    template_name = 'registration/user_update.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Malumotlaringiz yangilandi!')
        return super().form_valid(form)
    
    def get_object(self, queryset = None):
        return self.request.user

class UserProfileView(DetailView):
    template_name = 'registration/profile.html'
    model = Users
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user
    
class GetPremiumView(View):
    template_name = 'registration/get_premium.html'
    model = Users
    success_url = reverse_lazy('profile')

    def post(self, request, *args, **kwargs):

        request.user.is_premium = True
        request.user.limit_date = timezone.now() + timedelta(days=30)
        request.user.save()

        return redirect('profile')
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def get_object(self):
        return self.request.user