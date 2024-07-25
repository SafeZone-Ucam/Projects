from django.http import JsonResponse

def registers(request):
    data = { "Nome": "Gustavo" }
    return JsonResponse(data)
# Create your views here.
