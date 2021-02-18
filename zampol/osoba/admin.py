from django.contrib import admin
from django.utils.translation import gettext as _
from .models import MilitaryRank, Platoon, ServiseID, Unit, OfficialPosition, Company


class ServiseIDAdmin(admin.ModelAdmin):
    fieldsets = (
        # (None, {
        #    'fields': ('field1', 'field2', 'field3')
        # }),
        (_('Main data'), {
            'fields': ('name', 'sename', 'third_name', 'birth_date')
        }),
        (_('Unit'), {
            'fields': ('military_ranks', 'official_position', 'unit', 'platoon')

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

