from django.db import models

class Contacts(models.Model):
    Name = models.CharField(max_length=255)
    Surname = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Town = models.CharField(max_length=255)
    Street = models.CharField(max_length=255)
    Url = models.CharField(max_length=255)
    Photo = models.CharField(max_length=255)