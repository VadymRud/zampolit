from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from django.utils import formats
from pprint import pprint
from docxtpl import DocxTemplate
from pathlib import Path
from django.conf import settings
from staff.models import Staff
import os
from datetime import datetime, date


def get_doc_tpl(staff_id, tpl_name, ctx):
    p = settings.BASE_DIR 
    p1=Path(*p.parts[:-1])
    p_doc = p1 / 'doc_templates'
    staff = Staff.objects.get(pk=staff_id)
    tpl_name = '{}.docx'.format(tpl_name)
    doc = DocxTemplate(str(p_doc / tpl_name))
    doc.render(ctx)
    doc_path_in_home = '{}_{}_{}'.format(staff.ocoba.name, staff.ocoba.sename, staff.ocoba.third_name)
    print(doc_path_in_home)
    if not os.path.exists(Path.home() /doc_path_in_home):
        os.mkdir(Path.home() /doc_path_in_home)
    doc_save = Path.home() /doc_path_in_home/tpl_name
    doc.save(doc_save)
    os.startfile(doc_save)

class GetDocumentProbaAJAX(View):
   
    def post(self, request):
        pass
        
        #staff = Staff.objects.get(pk=request.POST.get('id_osoba'))
        # today = datetime.now()
        # date_uk = formats.date_format(today, format="YEAR_MONTH_FORMAT", use_l10n=True)
        
        
        # context = { 'military_rank' : staff.ocoba.military_ranks.name, 'sename':  staff.ocoba.sename,
        #  'name':staff.ocoba.name, 'thname': staff.ocoba.third_name, 'date': date_uk}
        # get_doc_tpl(staff_id = request.POST.get('id_osoba'), tpl_name= 'F5', ctx=context)
        # pprint(request.POST.get('id_osoba'))
        # return JsonResponse({'result': 'saved'})


class GetDocumentF5AJAX(View):
    def post(self, request):
        print(request.POST.get('id_staff'))
        staff = Staff.objects.get(pk=request.POST.get('id_staff'))
        today = date.today()
        date_locale = formats.date_format(today, format='"d" E Y', use_l10n=True)
        context = { 'military_rank' : staff.ocoba.military_ranks.name, 'sename':  str(staff.ocoba.sename).upper(),
            'name':staff.ocoba.name, 'thname': staff.ocoba.third_name, 'date': date_locale}
        get_doc_tpl(staff_id = request.POST.get('id_staff'), tpl_name= 'F5', ctx=context)
        pprint(request.POST.get('id_staff'))
        return JsonResponse({'result': 'saved'})
