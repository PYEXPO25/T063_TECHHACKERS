from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'CMS'

urlpatterns = [
    path('',views.start, name='start'),
    path('home/', views.home, name='home'),
    path('home/adminlogin/', views.adminlogin, name='adminlogin'),
    path('home/userlogin/', views.userlogin, name='userlogin'),
    path('home/userlogin/complaints/',views.complaints_view, name='complaints'),
    path('home/adminlogin/dashboard/', views.admin_dashboard, name="admindashboard"),
    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path('home/about', views.about, name='about'),
    path('home/contact', views.contact, name="contact"),
    path('home/userlogin/complaints/track/', views.track, name="track"),
]
