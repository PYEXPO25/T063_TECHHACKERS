from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'CMS'

urlpatterns = [
    path('',views.home, name='home'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogin/complaints/',views.complaints_view, name='complaints'),
]
7