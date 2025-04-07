from django import forms
from .models import News, Comment


class NewsForm(forms.ModelForm):
    title = forms.CharField(label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Überschrift angeben...', 'class':"form__title"}))

    message = forms.CharField(label='',
                    widget=forms.Textarea(attrs={'placeholder': 'Was möchten Sie mitteilen?', 'class':"form__message"}))

    class Meta:
        model = News
        fields = ['title', 'message']
        widgets = {
        }


class CommentForm(forms.ModelForm):

    text = forms.CharField(label='',
                    widget=forms.Textarea(attrs={'placeholder': 'Kommentieren...', 'class':"form__message"}))

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'user': forms.HiddenInput(),
            'news': forms.HiddenInput(),
        }
