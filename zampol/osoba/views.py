from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from base64 import b64encode
from .models import MilitaryRank, Platoon, ServiseID, Unit


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_blob'] = 1
        # context['image_blob'] = b64encode(ServiseID.objects.get(id=2).image3x4).decode()
        return context


class AjaxNameInAccs(View):
    def post(self, request):
        username = request.GET.get('username', None)
        data = {
            'is_present': 'hhhhh'
        }
        return JsonResponse(data)


