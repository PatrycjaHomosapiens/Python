# ten plik to wzorzec adresów URL

from django.urls import path
from . import views

# budujemy wzorzec:

urlpatterns = [

    path('', views.contactList, name='contactList'),
    path('contact/new', views.contactNew, name='contactNew'),
]