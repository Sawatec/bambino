from django.shortcuts import render
from django_tables2 import SingleTableView
from django.contrib.auth.models import User
from kinderübersicht.models import Kind, Gruppe

from account.models import UserProfile
from verwaltung.forms import UserUpdateForm, UsertypeSelectForm, AprovedForm, GruppeSelectForm
from verwaltung.tables import UserTable, KinderTable


# Create your views here.
def user_list(request):
    table = UserTable(User.objects.all())
    my_form = UsertypeSelectForm()
    if request.method == 'POST':
        my_form = UsertypeSelectForm(request.POST)
        usertype = request.POST['benutzertyp']
        print(usertype)
        if usertype == 'AL':
            table = UserTable(User.objects.all())
        else:
            table = UserTable(User.objects.all().filter(userprofile__user_type=usertype))

    context = {
        'form': my_form,
        'table': table,
    }
    return render(request, "userVerwaltung.html", context)


def showUpdateUser(request, **kwargs):
    user_id = kwargs['pk']
    benutzer = User.objects.get(id=user_id)
    profil = benutzer.userprofile

    if request.method == 'POST':
        form = UsertypeSelectForm()
        userForm = UserUpdateForm(request.POST, instance=benutzer)
        userForm.save()
        userprofileForm = AprovedForm(request.POST, instance=profil)
        table = UserTable(User.objects.all())
        userprofileForm.save()
        context = {'form': form,
                   'table': table
                   }
        return render(request, "userVerwaltung.html", context)

    userForm = UserUpdateForm(initial={
            'username': benutzer.username,
            'first_name': benutzer.first_name,
            'last_name': benutzer.last_name,
            'email': benutzer.email,
        })

    userprofileForm = AprovedForm(initial={
            'is_aproved': profil.is_aproved,
        })

    context = {'userForm': userForm,
               'userprofileForm': userprofileForm,
               'benutzer': benutzer
               }
    return render(request, "userUpdate.html", context)


def deleteUser(request, **kwargs):
    user_id = kwargs['pk']
    User.objects.get(id=user_id).delete()
    table = UserTable(User.objects.all())
    context = {
               'table': table
               }
    return render(request, "userVerwaltung.html", context)


def child_list(request):
    table = KinderTable(Kind.objects.all())
    my_form = GruppeSelectForm()
    if request.method == 'POST':
        my_form = GruppeSelectForm(request.POST)
        gruppe = request.POST['gruppe']

        table = KinderTable(Kind.objects.all().filter(gruppe__gruppenname=Gruppe.objects.get(id=gruppe)))

    context = {
        'form': my_form,
        'table': table,
    }
    return render(request, "kinderVerwaltung.html", context)


def deleteUser(request, **kwargs):
    kind_id = kwargs['pk']
    Kind.objects.get(id=kind_id).delete()
    table = UserTable(Kind.objects.all())
    context = {
               'table': table
               }
    return render(request, "kinderVerwaltung.html", context)
