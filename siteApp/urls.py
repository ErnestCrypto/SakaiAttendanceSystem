from django.contrib import admin
from django.urls import path
from . import views

app_name = "siteAppUrls"

urlpatterns = [
    path('', views.loginPage, name="loginPage"),
    path('attendance', views.attendancePage, name="attendancePage"),
    path('dcit_202', views.attendance2Page, name="attendance2Page"),
    
    path('error', views.errorPage, name="errorPage"),
    path('home', views.homePage, name="homePage"),
    path('record', views.recordPage, name="recordPage"),
    path('success', views.successPage, name="successPage"),
    path('take_attendance', views.takeAttendance, name="takeAttendance"),
    path('take_attendance2', views.takeAttendance2, name="takeAttendance"),
    
    
]
