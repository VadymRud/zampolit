from django.shortcuts import render
from django.views.generic import TemplateView
from base64 import b64encode
from .models import MilitaryRank, Platoon, ServiseID, Unit


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_blob'] = 1
        # context['image_blob'] = b64encode(ServiseID.objects.get(id=2).image3x4).decode()
        return context



