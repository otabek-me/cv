from django import forms
from users.models import Users
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login' : "Email yoki parol noto'g'ri kiritildi",
    }

    username = forms.EmailField(
        label='Email kiriting',
        error_messages = {
            'required':'Email kiritish majburiy',
            'invalid':'Noto\'g\'ri formatda kiritildi!'
        },
        widget = forms.EmailInput(attrs={
            'placeholder':'Email kiriting'
        }

        )
    )
    password = forms.CharField(
        label='Parolingizni kiriting',
        error_messages={
            'required':'Parol kiritish majburiy!'
        },
        widget = forms.PasswordInput(attrs={
            'placeholder':'Parol kiriting'
        })
    )

class UserCreateForm(UserCreationForm):
    error_messages={
        'password_mismatch':'Parollar mos kelmadi'
    }

    class Meta:
        model = Users
        fields = ['email', 'first_name', 'last_name']
        error_messages = {
            'email': {
                'unique':'Bu email ro\'yxatdan o\'tgan!'
            }
        }

        email = forms.EmailField(
            label='Email manzili',
            error_messages={
                'required':'Email manzilini kiriting!',
                'invalid':'Email manzilini to\'g\'ri kiriting',
            },
            widget = forms.EmailInput(attrs={
                'placeholder':'Email manzilini kiriting...'
            }),
        )
        first_name = forms.CharField(
            label='Ism',
            widget=forms.TextInput(attrs={
                'placeholder':'Ismingizni kiriting...'
            })
        )
        last_name = forms.CharField(
            label='Ism',
            widget=forms.TextInput(attrs={
                'placeholder':'Familiyangizni kiriting...'
            })
        )

        password1 = forms.CharField(
            label='Parol yarating',
            error_messages={
                'required':"Parolni kiriting!"
            },
            widget=forms.PasswordInput(attrs={
                'placeholder':'Parol'
            })
        )
        password2 = forms.CharField(
            label='Parolni takrorlang',
            error_messages={
                'required':"Parolni kiriting!"
            },
            widget=forms.PasswordInput(attrs={
                'placeholder':'Parol tasdiqlash'
            })
        )

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder':'Ismingizni kiriting...'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Familiya kiriting...'}),
        }