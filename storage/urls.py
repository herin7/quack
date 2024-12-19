from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page='home'), name="logout"),  # Add logout here
    path("accounts/", include("django.contrib.auth.urls")),
    path('space/<slug:custom_url>/', views.user_space, name='user_space'),
    path('delete/<str:custom_url>/', views.delete_space, name='delete_space'),
    path('profile/', views.user_profile, name='user_profile'),
    path('view/<slug:custom_url>/', views.public_space, name='public_space'),
    path("signup/", views.authview, name="authView"),
]
