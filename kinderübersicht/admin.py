from django.contrib import admin
from .models import Kind, Mitteilung, Gruppe, Entwicklernotiz

# Register your models here.
admin.site.register(Kind)
admin.site.register(Mitteilung)
admin.site.register(Gruppe)
admin.site.register(Entwicklernotiz)