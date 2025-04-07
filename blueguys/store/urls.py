from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store_page, name='store-page'),  # Fixed name here
    path('store/register/', views.register, name='register'),
    path('store/login/', views.login, name='login'),
    path('store/logout/', views.logout, name='logout'),
    path('store/item/<int:id>/', views.item_detail, name='item-detail'),  # for item detail page
]
