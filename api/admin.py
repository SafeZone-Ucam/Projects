from django.contrib import admin
from api.models import MapPoint

class MapPoints(admin.ModelAdmin):
    list_display = ('id','pointX', 'pointY')
    list_display_links = ('id')

    admin.site.register(MapPoint)
