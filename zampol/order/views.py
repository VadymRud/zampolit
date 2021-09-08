from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from pprint import pprint


class GetDocumentProbaAJAX(View):
    def post(self, request):
    # <view logic>
        pprint(request.POST.get('id_osoba'))
        return JsonResponse({'result': 'huy'})
