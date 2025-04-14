from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.home, name='home'),  # 👈 this matches the homepage

    path('about/', views.aboutpage, name='aboutpage'),
    path('blog/', views.blogpage, name='blog'),
    path('change-address/', views.change_address, name='change_address'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('write-letter/', views.write_letter, name='write_letter'),
    path('write-letter-2/', views.write_letter2, name='write_letter2'),
    path('write-letter-3/', views.write_letter3, name='write_letter3'),
    path('write-letter-4/', views.write_letter4, name='write_letter4'),
     
    # Auth URLs
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
