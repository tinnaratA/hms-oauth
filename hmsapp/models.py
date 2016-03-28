from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    blood_type = models.CharField(max_length=2)
    allergies = models.TextField()

    def __str__(self):
        return self.first_name

class Physician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    specialise = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.first_name
