from django import forms
from .models import Kind, Mitteilung, Entwicklernotiz


class SearchForm(forms.ModelForm):

    nachname = forms.CharField(label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Nachname', 'class':"suche__surname"}))

    class Meta:
        model = Kind
        fields = ['nachname']


class EntwicklernotizForm(forms.ModelForm):
    text = forms.CharField(label='',
                    widget=forms.Textarea(attrs={'placeholder': 'Ihre Entwicklungsnotiz', 'class':"suche__surname"}))

    class Meta:
        model = Entwicklernotiz
        fields = ['text', 'type']
        widgets = {
            'type': forms.Select(choices=Entwicklernotiz.NOTIZ_TYP),
            'user': forms.HiddenInput(),
            'mitteilung': forms.HiddenInput(),
            'kind': forms.HiddenInput(),
        }


class MitteilungForm(forms.ModelForm):
    text = forms.CharField(label="", help_text="", widget=forms.Textarea())
    class Meta:
        model = Mitteilung
        fields = ['text']
        widgets = {
            'user': forms.HiddenInput(),
        }
