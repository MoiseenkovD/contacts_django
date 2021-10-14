from django.contrib import admin
from django.urls import path
from contacttable.api import contacts
from contacttable.api import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts.ContactsApi.as_view()),
    path('contacts/<int:id>/', contact.ContactApi.as_view()),
]
