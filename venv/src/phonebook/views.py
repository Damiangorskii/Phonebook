from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView
from .models import Osoba, Telefon, Email
from .forms import OsobaForm, TelefonForm, EmailForm
from .filters import OsobaFilter,  TelefonFilter, EmailFilter



# Create your views here.


class OsobaListView(ListView):
    model = Osoba
    template_name = 'phonebook/phonebook_list.html'
    form_class = OsobaForm
    queryset = Osoba.objects.all()


def phonebook_list_view(request):
    queryset = Osoba.objects.all()

    myFilterOsoba = OsobaFilter(request.GET, queryset=queryset)
    queryset = myFilterOsoba.qs

    context = {
        "object_list": queryset,
        "myFilterOsoba": myFilterOsoba,
    }
    return render(request, "phonebook/phonebook_list.html", context)

def phonebook_detail_view(request, id):
    obj = get_object_or_404(Osoba, id=id)

    telefon = (Telefon.objects.filter(osoba_id=id))
    myFilterTelefon = TelefonFilter(request.GET, queryset=telefon)
    telefon = myFilterTelefon.qs

    email = Email.objects.filter(osoba_id=id)
    myFilterEmail = EmailFilter(request.GET, queryset=email)
    email = myFilterEmail.qs

    context = {
        'object': obj,
        'telefon': telefon,
        'myFilterTelefon': myFilterTelefon,
        'email': email,
        'myFilterEmail': myFilterEmail
    }
    return render(request, "phonebook/phonebook_detail.html", context)

def phonebook_create_view(request):
    osoba = OsobaForm(request.POST or None)
    if osoba.is_valid():
        osoba.save()
        return HttpResponseRedirect('../')
    context = {
        'osoba': osoba,
    }
    return render(request, "phonebook/phonebook_create.html", context)

def phonebook_update_view(request, id=id):
    obj = get_object_or_404(Osoba, id=id)
    osoba = OsobaForm(request.POST or None, instance=obj)
    if osoba.is_valid():
        osoba.save()
        return HttpResponseRedirect('../')
    context = {
        'osoba': osoba
    }
    return render(request, "phonebook/phonebook_update.html", context)


def phonebook_delete_view(request, id):
    obj = get_object_or_404(Osoba, id=id)
    telefon = Telefon.objects.filter(osoba_id=id)
    email = Email.objects.filter(osoba_id=id)
    if request.method == "POST" and not telefon and not email:
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "phonebook/phonebook_delete.html", context)

def phonebook_add_phone_number_view(request, id):
    telefonObj = Telefon.objects.create(osoba_id=id)
    telefon = TelefonForm(request.POST or None, instance=telefonObj)
    if telefon.is_valid():
        telefon.save()
        return HttpResponseRedirect('../')
    context = {
        'telefon': telefon,
    }
    return render(request, "phonebook/phonebook_add_phone_number.html", context)

def phonebook_add_adress_email_view(request, id):
    emailObj = Email.objects.create(osoba_id=id)
    email = EmailForm(request.POST or None, instance=emailObj)
    if email.is_valid():
        email.save()
        return HttpResponseRedirect('../')
    context = {
        'email': email,
    }
    return render(request, "phonebook/phonebook_add_adress_email.html", context)
