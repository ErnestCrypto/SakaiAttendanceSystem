from django.contrib import admin
from .models import *
# Registering our models

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'student_id', 'pin','classes_present','total_classes',
    ]


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = [
        'student', 'present', 'date',
    ]

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        'course', 'longitude', 'latitude',
    ]


