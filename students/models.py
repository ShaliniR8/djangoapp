from django.db import models


# Create your models here.
class Student(models.Model):
     Roll = models.IntegerField()
     Name = models.CharField(max_length=50)
     Uni = models.CharField(max_length=100)
     GPA = models.FloatField(default=0.0)

class 