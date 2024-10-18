# blog/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),  # New path for the Home page
    path('about/', views.about, name='about'),  # New path for the About page
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('download_image/', views.download_image, name='download_image'),
    path('delete_account/', views.delete_account, name='delete_account'),
]
