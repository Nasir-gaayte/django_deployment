from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register, name='register'),
    path('profile/',views.profile,name='profile'),
    path('logout/',auth_view.LogoutView.as_view (template_name='sys_app/logout.html'), name='logout'),
    path('login/',auth_view.LoginView.as_view (template_name='sys_app/login.html'), name='login'),
]
