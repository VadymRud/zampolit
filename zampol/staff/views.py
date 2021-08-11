from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View, DetailView, ListView
from base64 import b64encode
from osoba.models import MilitaryRank, Platoon, ServiseID, Unit
from .models import Staff, SHPK, PidrozdilName, Name, Shtatka


class StaffListView(ListView):
    model = Staff


class PidrozdilNameView(ListView):
    # model = PidrozdilName
    
    def get_queryset(self):
        # self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Shtatka.objects.all()


class ShtatkaView(TemplateView):
    template_name = 'staff\\pidrozdilname_list.html'

    def get(self, request, *args, **kwargs):
        pidrname = PidrozdilName.objects.filter(active=1)
        name = Name.objects.all()
        sht = Shtatka.objects.all()

        return render(request, self.template_name, context={'pidr': pidrname, 'names':name,
        'shtatka':sht})


class StaffDetailView(DetailView):
    #model = Staff
    def get_queryset(self):
        st= Staff.objects.get(pk=1)
        return Staff.objects.all()

