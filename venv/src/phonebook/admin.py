from django.contrib import admin
from .models import Osoba, Telefon, Email


# Register your models here.


admin.site.register(Telefon)
admin.site.register(Email)
admin.site.register(Osoba)
