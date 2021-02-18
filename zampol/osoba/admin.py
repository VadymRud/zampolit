from django.contrib import admin
from .models import MilitaryRank, Platoon, ServiseID, Unit, OfficialPosition, Company
admin.site.register(Company)
admin.site.register(MilitaryRank)
admin.site.register(Platoon)
admin.site.register(ServiseID)
admin.site.register(Unit)
admin.site.register(OfficialPosition)
