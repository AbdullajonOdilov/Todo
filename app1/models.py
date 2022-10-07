from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    fullname = models.CharField(max_length=50)
    guruh = models.CharField(max_length=50,blank=True)
    st_id = models.CharField(max_length=50,blank=True)
    tel = models.CharField(max_length=50,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):return self.fullname

class Todo(models.Model):
    title = models.CharField(max_length=50)
    time = models.DateTimeField()
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    def __str__(self):return self.title



