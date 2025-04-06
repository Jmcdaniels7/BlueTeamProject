from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage route
    path('store/', views.store_page, name='store_page'),  # Route for the store page
    path('store/register/', views.register, name='register'),  # Registration page
    path('store/login/', views.login, name='login'),  # Login page
    path('store/logout/', views.logout, name='logout'),  # Logout page
]
