from .models import Osoba, Email, Telefon
from django import forms


class OsobaForm(forms.ModelForm):
    imie = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your name", "max_length": "50"}))
    nazwisko = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your surname", "max_length": "50"}))

    class Meta:
        model = Osoba
        fields = [
            'imie',
            'nazwisko'
        ]


class TelefonForm(forms.ModelForm):
    telefon = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={"placeholder": "Your phone number", "max_length": "50"}))

    class Meta:
        model = Telefon
        fields = [
            'telefon',
        ]

    def clean_telefon(self, *args, **kwargs):
        telefon = self.cleaned_data.get("telefon")
        if not telefon.isdigit():
            raise forms.ValidationError("This is not a valid phone number")
        else:
            return telefon


class EmailForm(forms.ModelForm):
    email = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={"placeholder": "Your email adress"}))

    class Meta:
        model = Email
        fields = [
            'email',
        ]

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not '@' in email:
            raise forms.ValidationError("This is not a valid email adress")
        else:
            return email
