from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from contacttable.models import Contacts


class ContactsApi(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(Contacts)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        c1 = Contacts(Name="vlad", Surname="0004", Phone="111")
        c1.save()
        return HttpResponse("success")
