from django.http import JsonResponse
from rest_framework import viewsets
from api.models import MapPoint

def registers(request):
    data = { "Nome": "Gustavo" }
    return JsonResponse(data)

class MapPointViewSets(viewsets.ModelViewSet):
    queryset = MapPoint.objects.all()
