from django.db import models
from django.contrib import admin

class MapPoint (models.Model):
    userId = models.ForeignKey
    pointX = models.FloatField(null=False, blank=False)
    pointY = models.FloatField(null=False, blank=False)

