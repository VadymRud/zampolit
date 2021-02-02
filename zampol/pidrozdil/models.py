from django.db import models


class Pidrozdil(models.Model):
    name = models.CharField(max_length=512)