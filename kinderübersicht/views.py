from django.shortcuts import render

from kinderübersicht.forms import SearchForm, EntwicklernotizForm, MitteilungForm
from .models import Kind, Mitteilung, Entwicklernotiz, Gruppe


# Create your views here.


def showChildrenView(request):
    kids = Kind.objects.all()
    gruppen = Gruppe.objects.all()
    if request.method == 'POST':
        my_form = SearchForm(request.POST)
        search_string = request.POST['nachname']
        print(search_string)
        kids = Kind.objects.filter(nachname=search_string)
        my_form = SearchForm()
        gruppen = set()
        gruppen.add(kids[0].gruppe)
        context = {'form': my_form,
                   'kids': kids,
                   'gruppen': gruppen,
                   'show_results': True}
        return render(request, 'kinderübersicht.html' , context)

    else:
        my_form = SearchForm()
        context = {'form': my_form,
                   'kids': kids,
                   'gruppen': gruppen,
                   'show_results': False}
        return render(request, 'kinderübersicht.html', context)


def showInfoChild(request, **kwargs):
    child_id = kwargs['pk']
    child = Kind.objects.get(id=child_id)

    # Add comment
    if request.method == 'POST':
        if 'Entwicklungsnotiz' in request.POST:
            print("Post akzeptiert")
            form = EntwicklernotizForm(request.POST)
            print("form gespeichert")
            form.instance.user = request.user
            form.instance.author = request.user.userprofile.get_full_name()
            print("instance.user")
            form.instance.kind = child
            print("instance.child")
            if form.is_valid():
                form.save()
                print("wurde gespeichert")
            else:
                print("form ist nicht valide")
                print(form.errors)
        elif 'Mitteilung' in request.POST:
            print("Post akzeptiert")
            form = MitteilungForm(request.POST)
            print("form gespeichert")
            form.instance.user = request.user
            form.instance.author = request.user.userprofile.get_full_name()
            print("instance.user")
            form.instance.kind = child
            print("instance.child")
            if form.is_valid():
                form.save()
                print("wurde gespeichert")
            else:
                print("form ist nicht valide")
                print(form.errors)

    entwicklungsnotizen = Entwicklernotiz.objects.filter(kind=child)
    mitteilungen = Mitteilung.objects.filter(kind=child)
    context = {'child': child,
               'entwicklungsnotizen': entwicklungsnotizen,
               'mitteilungen': mitteilungen,
               'entwicklungs_form': EntwicklernotizForm,
               'mitteilungs_form': MitteilungForm}
    return render(request, 'kindinformation.html', context)
