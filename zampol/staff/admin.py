from django.contrib import admin
from django.contrib import admin
from django.utils.translation import gettext as _
from .models import (SHPK, Staff)

admin.site.register(SHPK)
admin.site.register(Staff)
