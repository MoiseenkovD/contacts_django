from django.db import models
from rest_framework import serializers

class Contacts(models.Model):
    Name = models.CharField(max_length=255)
    Surname = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Town = models.CharField(max_length=255)
    Street = models.CharField(max_length=255)
    Url = models.CharField(max_length=255)
    Photo = models.FileField(upload_to='photos')

    @property
    def image_url(self):
        from django.contrib.sites.models import Site

        domain = Site.objects.get_current().domain
        url = 'http://{domain}'.format(domain=domain)

        if self.Photo and hasattr(self.Photo, 'url'):
            return url + self.Photo.url
        else:
            return ""

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"