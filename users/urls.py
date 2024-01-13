from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from .views import display_products, display_orders,user_profile,user_logout , login_view , edit_product, delete_product


app_name = 'users' 

urlpatterns = [
   path('vendor/', login_view, name='login'),
   path('dashboard/', display_products, name='vendor'), 
   path('add/', views.add_product, name='add-products'),
   path('orders/', display_orders, name='orders'),
   path('edit-product/<int:product_id>/', edit_product, name='edit-product'),
   path('profile/', user_profile, name='profile'),
   path('logout/', user_logout, name='logout'),
   path('delete-product/<int:product_id>/', delete_product, name='delete-product'),
]


