from django.contrib import admin
from django.utils.translation import gettext as _
from .models import StatusOrder, Order


class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Main data'), {
            'fields': ('order_number', 'order_date', 'name', 'osoba',  'appruve', 
            'appruve_date', 'status')
        }),
        
    )

admin.site.register(StatusOrder)
admin.site.register(Order, OrderAdmin)
