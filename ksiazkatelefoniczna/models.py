from django.db import models

class Contact(models.Model):        # dziedziczenie models, zawsze musi być

    firstName = models.CharField(max_length=100, default='', blank=False, null=False)  # CharField to pole tekstowe
                                                        # ustawiamy max długość na 100, że nie może być puste
    lastName = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, default='', blank=True, null=True)    # pole dedykowane do maila
    phone = models.CharField(max_length=100, default='', blank=True, null=True)




# Create your models here.
