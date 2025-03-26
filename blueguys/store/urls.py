from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/home/', views.homepage, name='homepage'),
    path('store/register/', views.register, name='register'),
    path('store/login/', views.login, name='login'),
    path('store/logout/', views.logout, name='logout'),
    path('store/chatbot/', views.chatbot, name='chatbot'),
]