from django.shortcuts import render
from contacttable.models import Contacts
from django.http import HttpResponse


def create(request):
    c1 = Contacts(Name="alex", Surname="0001", Phone="777")
    c1.save()
    return HttpResponse("ok")

