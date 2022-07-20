from django.db import models
class Student(models.Model):
 nombre = models.CharField(max_length=50)
 apellidos = models.CharField(max_length=50)
 edad = models.IntegerField()
 email = models.EmailField()

