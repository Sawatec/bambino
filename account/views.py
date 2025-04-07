from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CreateUserForm
from .models import UserProfile
from kinderübersicht.models import Kind
from django import forms


class CreateUser(generic.CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'create_user.html'

    def form_valid(self, form, ):
        data = form.cleaned_data
        mitgliedsnummer = data['mitgliedsnummer']
        kind = Kind.objects.filter(mitgliedsnummer=mitgliedsnummer)
        nutzerart = mitgliedsnummer.split("-")[1]
        if mitgliedsnummer:
            print("es gibt eine nummer")
            if nutzerart == "ED" or nutzerart == "A":
                print("yesss")
                createUser(data, mitgliedsnummer, nutzerart)
                return redirect('login')

            elif not kind and nutzerart == "PA":
                print("gibt keine kinder")
                return redirect('warning')

            elif not Kind.objects.filter(mitgliedsnummer=mitgliedsnummer)[0].eltern_user:
                user = createUser(data, mitgliedsnummer, nutzerart)
                kind = Kind.objects.filter(mitgliedsnummer=mitgliedsnummer)[0]
                kind.eltern_user = user
                kind.save()
                return redirect('login')


def createUser(data, mitgliedsnummer, nutzerart):
    user = User.objects.create_user(username=data['username'],
                                    password=data['password'],
                                    first_name=data['first_name'],
                                    last_name=data['last_name'],
                                    email=data['email'],
                                    )
    userProfile = UserProfile.objects.create(user=user,
                                             kindergarten=data['kindergarten'],
                                             mitgliedsnummer=data['mitgliedsnummer'],
                                             user_type=nutzerart,
                                             )
