from django.db import models


# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=20)
    email = models.CharField(max_length=45)
    message = models.TextField()
