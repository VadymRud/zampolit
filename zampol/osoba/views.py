from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from django.http import JsonResponse
from base64 import b64encode
from .models import MilitaryRank, Platoon, ServiseID, Unit
from staff.models import Staff, Company


class HomePageView(ListView):
    template_name = 'home/index.html'
    def get_queryset(self):
        return Company.objects.order_by('unik')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['staffs'] = Staff.objects.order_by('unicum')

    #     # context['image_blob'] = b64encode(ServiseID.objects.get(id=2).image3x4).decode()
    #     return context


class AjaxNameInAccs(View):
    def post(self, request):
        username = request.GET.get('username', None)
        data = {
            'is_present': 'hhhhh'
        }
        return JsonResponse(data)


