from django.urls import path
from cv_app.views import CreateCVView, UserCVDetailView, UserCVListView

urlpatterns = [
    path('create/', CreateCVView.as_view(), name='create-cv'),
    path('my-cv/', UserCVListView.as_view(), name='user-cv'),
    path('cv/detail/<int:pk>/', UserCVDetailView.as_view(), name='cv-detail'),
]
