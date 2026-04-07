from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.models import Users


class CV(models.Model):
    ism = models.CharField(max_length=50)
    familiya = models.CharField(max_length=50)
    t_sana = models.DateField()
    email = models.EmailField()
    phone = PhoneNumberField(verbose_name="telefon raqami")
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    languages = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=200)
    cv_text = models.TextField(blank=True, null=True, verbose_name="To‘liq CV matni")
    author = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='cv', verbose_name='author')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ism} {self.familiya}"