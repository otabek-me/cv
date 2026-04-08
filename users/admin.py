from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.admin import ModelAdmin
from .models import Users

@admin.register(Users)
class CustomUserAdmin(BaseUserAdmin, ModelAdmin):
    # Ro'yxatda ko'rinadigan ustunlar
    list_display = ("email", "is_premium", "requests", "limit_requests", "limit_date", "is_staff")
    list_filter = ("is_premium", "is_staff", "is_superuser")
    
    # Foydalanuvchi ma'lumotlarini tahrirlash sahifasi
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Shaxsiy ma'lumotlar", {"fields": ("first_name", "last_name")}),
        ("Premium Sozlamalar", {
            "fields": ("is_premium", "limit_date", "limit_requests", "requests"),
            "classes": ("tab",), # Unfold-da tab ko'rinishida chiqarish
        }),
        ("Huquqlar", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Muhim sanalar", {"fields": ("last_login", "date_joined")}),
    )
    
    # Qidiruv
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)