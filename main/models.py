from django.db import models
from django.urls import reverse


class Staff(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    
class Attendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    
    
    
    
    
    
    