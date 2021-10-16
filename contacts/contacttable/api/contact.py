from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from contacttable.models import Contacts
from rest_framework.views import APIView
from django.forms.models import model_to_dict

class ContactApi(APIView):
    @csrf_exempt
    def put(self, request, id):
        try:
            c1 = Contacts.objects.get(pk=id)

            name = request.data.get("name", c1.Name)
            surname = request.data.get("surname", c1.Surname)
            phone = request.data.get("phone", c1.Phone)
            address = request.data.get("address", c1.Address)
            country = request.data.get("country", c1.Country)
            town = request.data.get("town", c1.Town)
            street = request.data.get("street", c1.Street)
            url = request.data.get("url", c1.Url)
            photo = request.data.get("photo", c1.Photo)

            c1.Name = name
            c1.Phone = phone
            c1.Surname = surname
            c1.Address = address
            c1.Country = country
            c1.Town = town
            c1.Street = street
            c1.Url = url
            c1.Photo = photo

            c1.save()
        except Contacts.DoesNotExist:
            return HttpResponse('Такого ID не существует', status=404)

        return JsonResponse(model_to_dict(c1))

    @csrf_exempt
    def delete(self, request, id):
        try:
            wd = Contacts.objects.get(pk=id)
            wd.delete()
            return JsonResponse(model_to_dict(wd))
        except Contacts.DoesNotExist:
            return HttpResponse('Такого ID не существует', status=404)
