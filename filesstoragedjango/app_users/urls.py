from django.urls import path

from app_users import views


urlpatterns = [
    path('register/', views.RegisterUserAPIView.as_view()),
]
