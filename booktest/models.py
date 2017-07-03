from django.db import models


class AreaInfo(models.Model):
    atitle = models.CharField(max_length=50)
    aparent = models.ForeignKey('self', null=True, blank=True)
