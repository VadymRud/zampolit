from django.contrib import admin
from django.utils.translation import gettext as _
from .models import Status, Relocation

# Register your models here.
admin.site.register(Relocation)
admin.site.register(Status)
