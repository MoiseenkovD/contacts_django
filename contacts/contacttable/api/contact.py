from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from contacttable.models import Contacts

class ContactApi(View):
    @csrf_exempt
    def put(self, request, id, *args, **kwargs):
        c1 = Contacts.objects.get(pk=id)
        c1.Name = "lol"
        c1.Phone = "778787"
        c1.Surname = "kek"
        c1.save()
        return HttpResponse('success')

    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        return HttpResponse('success')
