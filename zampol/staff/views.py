from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View, DetailView, ListView
from base64 import b64encode
from osoba.models import MilitaryRank, Platoon, ServiseID, Unit
from .models import Staff, SHPK


class StaffListView(ListView):
    model = Staff
    
 
class StaffDetailView(DetailView):
    #model = Staff
    def get_queryset(self):
        st= Staff.objects.get(pk=1)
        return Staff.objects.all()

