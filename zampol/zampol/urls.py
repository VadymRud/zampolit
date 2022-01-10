from django.contrib import admin
from django.urls import path, include
from osoba.views import HomePageView
from staff.views import StaffListView, StaffDetailView, PidrozdilNameView, ShtatkaView
from django.conf.urls.static import static
from django.conf import settings
from order.views import GetDocumentF5AJAX, GetDocumentSСCardAJAX, GetDocumentInterviewAJAX
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


def okay(request):
    return HttpResponse('pretend-binary-data-here', content_type='image/jpeg')


urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('staff/', ShtatkaView.as_view(), name='staff_index'),
    path('ajax/getdocoment/f5', GetDocumentF5AJAX.as_view(), name='ajax_document_f5'),
    path('ajax/getdocoment/sc', GetDocumentSСCardAJAX.as_view(), name='ajax_document_sc'),
    path('ajax/getdocoment/interview', GetDocumentInterviewAJAX.as_view(), name='ajax_document_sc'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
