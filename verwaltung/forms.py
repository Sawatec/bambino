from django import forms
from django.contrib.auth.models import User
from account.models import UserProfile
from kinderübersicht.models import Gruppe,Kind

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]
        widgets = {
        }


class UsertypeSelectForm(forms.ModelForm):
    USERTYPE_CHOICE = [
        ('AL', 'Alle'),
        ('PA', 'Eltern'),
        ('ED', 'Erzieher'),
        ('GL', 'Gruppenleiter'),
        ('KM', 'Kitaleitung'),
        ('A', 'Admin')
    ]
    benutzertyp = forms.ChoiceField(choices=USERTYPE_CHOICE, widget=forms.Select(), required=True)

    class Meta:
        model = User
        fields = ('benutzertyp',)
        widgets = {
        }


class GruppeSelectForm(forms.ModelForm):
    gruppe = forms.ModelChoiceField(queryset=Gruppe.objects.all())

    class Meta:
        model = Kind
        fields = ('gruppe',)
        widgets = {
        }


class AprovedForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['is_aproved',]
        widgets = {
        }
