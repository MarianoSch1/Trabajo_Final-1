from django.shortcuts import render
from blog_opiniones.models import Configuracion
def index(request):
    configuracion = Configuracion.objects.first()
    return render(request, 'blog_opiniones/index.html', {'configuracion':configuracion})