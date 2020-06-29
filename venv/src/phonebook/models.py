from django.db import models
from django.urls import reverse

# Create your models here.
class Osoba(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Osoby"

    def __str__(self):
        return self.imie+" "+self.nazwisko

    def get_absolute_url(self):
        return reverse("phonebook:phonebook-detail", kwargs={"id": self.id})

class Telefon(models.Model):
    osoba = models.ForeignKey(Osoba, editable=True, default=1, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Telefony"

    def __str__(self):
        return self.telefon



class Email(models.Model):
    osoba = models.ForeignKey(Osoba, editable=True, default=1, on_delete=models.CASCADE)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Emaile"

    def __str__(self):
        return self.email




