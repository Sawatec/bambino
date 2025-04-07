from django.db import models
from django.contrib.auth.models import User


KINDERGÄRTEN_CHOICES = [
    ('Kita-Fröbel', 'Kita-Fröbel'),  # Wert und lesbare Form
    ('Kita-Abenteuerwelt', 'Kita-Abenteuerwelt'),
    ('Kita-Rübchen', 'Kita-Rübchen'),
]
#Wofür Usertype? Wählt der User beim Registrieren seine Rolle?
USERTYPE_CHOICE = [
    ('PA', 'Eltern'),  # Wert und lesbare Form
    ('ED', 'Erzieher'),
    ('GL', 'Gruppenleiter'),
    ('KM', 'Kitaleitung'),
    ('A', 'Admin')
]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kindergarten = models.CharField(max_length=50,
                                    choices=KINDERGÄRTEN_CHOICES,
                                    )
    user_type = models.CharField(max_length=50,
                                 choices=USERTYPE_CHOICE,
                                 default="Eltern",
                                 )
    is_aproved = models.BooleanField(default=False)
    mitgliedsnummer = models.CharField(max_length=10)

    def get_full_name(self):
        return self.user.first_name + " " + self.user.last_name

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' (' + ')'
