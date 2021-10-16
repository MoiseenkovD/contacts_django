from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from contacttable.models import Contacts
from rest_framework.views import APIView
from django.db.models import Q
from django.forms.models import model_to_dict


class ContactsApi(APIView):
    def get(self, request):
        search = request.query_params.get('search')

        if search is not None:
            c1 = Contacts.objects.filter(Q(Name=search) | Q(Surname=search))
        else:
            c1 = Contacts.objects.all()

        return JsonResponse(list(c1.values()), safe=False)

    @csrf_exempt
    def post(self, request):
        name = request.data.get("name")
        surname = request.data.get("surname")
        phone = request.data.get("phone")
        address = request.data.get("address", "")
        country = request.data.get("country", "")
        town = request.data.get("town", "")
        street = request.data.get("street", "")
        url = request.data.get("url", "")
        photo = request.data.get("photo", "")

        if name is None or surname is None or phone is None:
            return HttpResponse("Вы не ввели достаточно информации, повторите попытку", status=400)
        else:
            c1 = Contacts(Name=name, Surname=surname, Phone=phone, Address=address,
                          Country=country, Town=town, Street=street, Url=url, Photo=photo)
        c1.save()
        return JsonResponse(model_to_dict(c1), status=201)
