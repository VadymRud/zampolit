from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from pprint import pprint
from docxtpl import DocxTemplate
from pathlib import Path
from django.conf import settings
from staff.models import Staff
import os


def get_doc_tpl(staff_id, tpl_name):
    p = settings.BASE_DIR 
    p1=Path(*p.parts[:-1])
    p_doc = p1 / 'doc_templates'
    staff = Staff.objects.get(pk=staff_id)
    tpl_name = '{}.docx'.format(tpl_name)
    doc = DocxTemplate(str(p_doc / tpl_name))
    context = { 'military_rank' : staff.ocoba.military_ranks.name, 'sename':  staff.ocoba.sename,
         'name':staff.ocoba.name, 'thname': staff.ocoba.third_name}
    doc.render(context)
    doc_path_in_home = '{}_{}_{}'.format(staff.ocoba.name, staff.ocoba.sename, staff.ocoba.third_name)
    print(doc_path_in_home)
    if not os.path.exists(Path.home() /doc_path_in_home):
        os.mkdir(Path.home() /doc_path_in_home)
    doc_save = Path.home() /doc_path_in_home/tpl_name
    doc.save(doc_save)

class GetDocumentProbaAJAX(View):
    def post(self, request):
        # p = settings.BASE_DIR 
        # p1=Path(*p.parts[:-1])
        # p_doc = p1 / 'doc_templates'
        # doc = DocxTemplate("my_word_template.docx")
        # context = { 'company_name' : "World company" }
        # doc.render(context)
        # doc.save("generated_doc.docx")
        get_doc_tpl(staff_id = request.POST.get('id_osoba'), tpl_name= 'F5')
        pprint(request.POST.get('id_osoba'))
        return JsonResponse({'result': 'saved'})
