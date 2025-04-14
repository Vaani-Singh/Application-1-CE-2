from django.contrib import admin
from django.urls import path, include
from application1 import views

urlpatterns = [
    path('about/', views.aboutpage, name='aboutpage'),

    path('admin/', admin.site.urls),
    path('', include('application1.urls')),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
]
