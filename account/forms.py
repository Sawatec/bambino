from django.contrib.auth.models import User
from django import forms
from account.models import KINDERGÄRTEN_CHOICES
from kinderübersicht.models import Kind


class CreateUserForm(forms.ModelForm):
    # Fields zusaetzlich zu User-Model
    kindergarten = forms.ChoiceField(choices = KINDERGÄRTEN_CHOICES,  widget=forms.Select(), required=True)
    mitgliedsnummer = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'kindergarten', 'mitgliedsnummer')
        widgets = {
            'password': forms.PasswordInput(),
        }

        def clean_mitgliedsnummer(self):
            data = self.cleaned_data.get('mitgliedsnummer')
            kind = Kind.objects.filter(mitgliedsnummer=data)
            if data:
                if not kind:
                    raise forms.ValidationError("Mitgliedsnummer falsch")

