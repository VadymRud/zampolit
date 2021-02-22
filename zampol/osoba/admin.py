from django.contrib import admin
from django.utils.translation import gettext as _
from .models import (MilitaryRank, Platoon, ServiseID, Unit, OfficialPosition, Company, 
                    Education, Creed, Nationality)


class ServiseIDAdmin(admin.ModelAdmin):
    fieldsets = (
        # (None, {
        #    'fields': ('field1', 'field2', 'field3')
        # }),
        (_('Main data'), {
            'fields': ('name', 'sename', 'third_name', 'birth_date')
        }),
        (_('Company'), {
            'fields': ('military_ranks', 'official_position', 'unit', 'platoon')

        }),
        (_('Info for Service begin'), {
            'fields': ('military_office', 'date_of_conscription', 'order_date', 'order_number')
            
        }),
        (_('General information'), {
            'fields': ('militaryID_seria', 'militaryID_number', 'ipn', 'orphan',
            'married', 'halforphan', 'work', 'mobilization', 'driveid', 'creed',
            'nationality', 'education', 'weapon')
            
        }),
        
        (_('Images'), {
            'fields': ('image_face3x4',)
            
        })
    )


admin.site.register(Company)
admin.site.register(MilitaryRank)
admin.site.register(Platoon)
admin.site.register(ServiseID, ServiseIDAdmin)
admin.site.register(Unit)
admin.site.register(OfficialPosition)
admin.site.register(Creed)
admin.site.register(Nationality)
admin.site.register(Education)
