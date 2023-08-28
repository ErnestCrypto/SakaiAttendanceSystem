from django.shortcuts import render
from .models import *
import requests
import json
# Create your models here.


def get_student(pk):
    try:
        student = Student.objects.get(student_id = pk)
        return student
    except:
        return None
        

def loginPage(request):
    context = {}     
    return render(request, 'index.html', context)
       

def homePage(request):
    if request.method == 'POST':
        student_id = request.POST.get('username')
        pin = request.POST.get('password')
        student_exists = get_student(student_id)
        print(student_id)
        if not student_exists:
            student = Student.objects.create(student_id=student_id,pin=pin)
        request.session['student_id'] = student_id
    context = {"student_id": student_id}
    
    return render(request, 'home.html', context)


def errorPage(request):
    student_id= request.session.get('student_id')
    context = {"student_id": student_id}
    return render(request, 'error.html', context)


def attendancePage(request):
    student_id= request.session.get('student_id')
    context = {"student_id": student_id}
    return render(request, 'attendance.html', context)


def recordPage(request):
    student_id= request.session.get('student_id')
    student = Student.objects.get(student_id=student_id)
    classes_missed =student.total_classes-student.classes_present
    context = {"student_id": student_id,
               "classes_present":student.classes_present,
               "total_classes":student.total_classes,
               "classes_missed":classes_missed,
               }
    return render(request, 'record.html', context)


def successPage(request):
    student_id= request.session.get('student_id')
    context = {"student_id": student_id}
    return render(request, 'success.html', context)





def get_ip_geolocation_data(ip_address):
    api_key = 'f5717dc070fb45d1ae361a31e761badf'
    api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=f5717dc070fb45d1ae361a31e761badf' + api_key
    response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=f5717dc070fb45d1ae361a31e761badf")
    return response.content



def takeAttendance(request):
    student_id= request.session.get('student_id')
    student = Student.objects.get(student_id=student_id)
    context = {"student_id": student_id}
    course = Location.objects.get(course="DCIT 402")
    course_longitude = course.longitude
    course_latitude = course.latitude
    course_location = float(course_longitude) + float(course_latitude)
    margin_error_plus = course_location + 10
    margin_error_minus = course_location - 10
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    geolocation_json = get_ip_geolocation_data(ip)
    geolocation_data = json.loads(geolocation_json)
    longitude = geolocation_data['longitude']
    latitude = geolocation_data['latitude'] 
    student_location = longitude + latitude
    if margin_error_minus < student_location and margin_error_plus > student_location: 
        Attendance.objects.create(student=student)
        student.classes_present =  int(student.classes_present) + 1
        student.save()
        print(student.classes_present)
        return render(request, 'success.html', context)
    return render(request, 'error.html', context)
    
