from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import CV

@admin.register(CV)
class CVAdmin(ModelAdmin):
    # Ro'yxat sahifasida ko'rinadigan ustunlar
    list_display = ("ism", "familiya", "email", "phone", "author", "created_at")
    
    # Filtrlash va qidiruv
    list_filter = ("created_at", "author")
    search_fields = ("ism", "familiya", "email", "skills")
    
    # Ma'lumotni tahrirlash sahifasini bo'limlarga (Tab) ajratish
    fieldsets = (
        ("Shaxsiy ma'lumotlar", {
            "fields": (
                ("ism", "familiya"), # Bir qatorda chiqarish uchun
                ("t_sana", "email"),
                "phone",
                "author",
            ),
        }),
        ("Malaka va Tajriba", {
            "fields": ("education", "experience", "skills"),
            "classes": ("tab",), # Unfold-da alohida tab qiladi
        }),
        ("Qo'shimcha", {
            "fields": ("languages", "hobbies", "cv_text"),
            "classes": ("tab",),
        }),
    )

    # Sana bo'yicha iyerarxiya (tepada navigatsiya hosil qiladi)
    date_hierarchy = "created_at"