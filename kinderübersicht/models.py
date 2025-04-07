from datetime import date
from django.db import models
from django.contrib.auth.models import User
import birthday


class Gruppe(models.Model):
    gruppenname = models.CharField(max_length=50)

    class Meta:
        ordering = ['gruppenname',]
        verbose_name = 'Gruppe'
        verbose_name_plural = 'Gruppen'

    def __str__(self):
        return self.gruppenname

    def __repr__(self):
        return self.gruppenname


class Kind(models.Model):
    vorname = models.CharField(max_length=50)
    nachname = models.CharField(max_length=50)
    zeitpunkt_des_beitritts = models.DateTimeField(auto_now_add=True)
    elternteil_1 = models.CharField(max_length=50)
    elternteil_2 = models.CharField(max_length=50)
    eltern_user = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name='parent_user',
                                    related_query_name='user',
                                    blank=True,
                                    null=True,
                             )
    gruppe = models.ForeignKey(Gruppe, on_delete=models.CASCADE)
    mitgliedsnummer = models.CharField(max_length=10)

    class Meta:
        ordering = ['vorname',]
        verbose_name = 'Kind'
        verbose_name_plural = 'Kinder'

    def get_full_name(self):
        return self.vorname + " " + self.nachname

    def get_message(self):
        messages = Mitteilung.objects.filter(kind=self)
        if not messages:
            return "keine Mitteilungen vorhanden"
        else:
            return messages.latest("erstellungs_datum").text

    def __str__(self):
        return self.vorname + ' ' + self.nachname

    def __repr__(self):
        return self.vorname + ' ' + self.nachname


class Mitteilung(models.Model):
    text = models.CharField(max_length=1000)
    erstellungs_datum = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)

    class Meta:
        ordering = ['erstellungs_datum',]
        verbose_name = 'Mitteilung'
        verbose_name_plural = 'Mitteilungen'

    def __str__(self):
        return self.kind.vorname + ' ' + self.kind.nachname

    def __repr__(self):
        return self.kind.vorname + ' ' + self.kind.nachname


class Entwicklernotiz(models.Model):
    NOTIZ_TYP = [
        ('SP', 'Sprache'),
        ('SOV', 'Sozialverhalten'),
        ('KO', 'Kognition'),
        ('FM', 'Feinmotorik'),
        ('GM', 'Grobmotorik'),
        ('KuP', 'Körper und Pflegebewusstsein'),
        ('SPV', 'Spielverhalten'),
        ('UB', 'Umgebungsbewusstsein'),
    ]

    text = models.CharField(max_length=500)
    erstellungs_datum = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    type = models.CharField(max_length=3,
                            choices=NOTIZ_TYP,
                            )
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-erstellungs_datum',]
        verbose_name = 'Entwicklernotiz'
        verbose_name_plural = 'Entwicklernotizen'

    def __str__(self):
        return self.type

    def __repr__(self):
        return self.type
