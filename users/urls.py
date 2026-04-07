from django.urls import path
from users.views import LoginView, SignUpView, UserProfileView, UserUpdateView, GetPremiumView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('sigup/', SignUpView.as_view(), name='signup'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('update/', UserUpdateView.as_view(), name='profile-update'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('get-premium/', GetPremiumView.as_view(), name='get-premium'),
    ]
