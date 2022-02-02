import django_tables2 as tables
from staff.models import Staff, Company


class Bootstrap4Table(tables.Table):
    country = tables.Column(linkify=True)
    continent = tables.Column(accessor="country__continent", linkify=True)

    class Meta:
        model = Company
        template_name = "django_tables2/bootstrap4.html"
        attrs = {"class": "table table-hover"}
        exclude = ("friendly",)
