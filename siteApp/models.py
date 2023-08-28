from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=255, default=None,null=True)
    pin = models.CharField(max_length=255, default=None,null=True)
    total_classes = models.IntegerField(default=24)
    classes_present = models.IntegerField(default=0)
    def __str__(self):
        return str(self.student_id)


class Attendance(models.Model):
    student = models.ForeignKey(
        Student, related_name='student', on_delete=models.CASCADE,null=True)
    present = models.BooleanField(default=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.student_id)


class Location(models.Model):
    course = models.CharField(max_length=255,default=None,null=True)
    longitude = models.CharField(max_length=255,default=None,null=True)
    latitude = models.CharField(max_length=255,default=None,null=True)
    






