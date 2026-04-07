from django import forms
from cv_app.models import CV


class CreateCVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ["ism", "familiya", "t_sana", "email", "phone", "education", "experience", "skills", "languages", "hobbies"]

        widgets = {
            't_sana': forms.DateInput(attrs={'type': 'date'}),
            'education': forms.Textarea(attrs={'rows': 3}),
            'experience': forms.Textarea(attrs={'rows': 4}),
            'skills': forms.Textarea(attrs={'rows': 2}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'placeholder': '+998901234567'}),
        }