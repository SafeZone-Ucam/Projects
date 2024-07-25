from django.contrib import admin
from django.urls import path
from api.views import registers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', registers)
]
