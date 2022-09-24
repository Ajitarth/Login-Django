from django.contrib import admin
from django.urls import path, include
from queryScraper import views
from django.contrib.auth import views as authentication_views




urlpatterns = [
    
    path('accept/', views.accept,name= "accept"),
    path('register/', views.register,name= "register"),
    path('', authentication_views.LoginView.as_view(template_name='queryScraper/login.html'),name= "login"),
    path('logout/', authentication_views.LogoutView.as_view(template_name='queryScraper/logout.html'),name= "logout"),
]
