from django.urls import path
from accounts import views

urlpatterns = [
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('kayıt-ol', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('accounts/password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
]