from django.contrib import admin
from .models import Reward, Penalty, TypePenalty, TypeReward, RewardOcoba, Interview

admin.site.register(Reward)
admin.site.register(Penalty)
admin.site.register(TypeReward)
admin.site.register(TypePenalty)
admin.site.register(RewardOcoba)
admin.site.register(Interview)
