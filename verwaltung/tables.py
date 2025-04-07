import django_tables2 as tables
from django.contrib.auth.models import User
from kinderübersicht.models import Kind
from account.models import UserProfile

class UserTable(tables.Table):
    change = tables.TemplateColumn('''
                                    <a href="/verwaltung/showUser/update_user/{{ record.id }}">Bearbeiten</a>
                                    <a href="/verwaltung/showUser/delete_user/{{ record.id }}"
                                    onclick="return confirm('Sind sie sicher dass sie den Benutzer löschen wollen?')">Löschen</a>''',
                                    verbose_name=u'Verwalten',
                                    )

    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff', 'is_active', 'last_login')


class KinderTable(tables.Table):
    change = tables.TemplateColumn('''
                                    <a href="/verwaltung/showUser/delete_user/{{ record.id }}"
                                    onclick="return confirm('Sind sie sicher dass sie den Benutzer löschen wollen?')">Löschen</a>''',
                                    verbose_name=u'Verwalten',
                                    )

    class Meta:
        model = Kind
        exclude = ('eltern_user','id',)
