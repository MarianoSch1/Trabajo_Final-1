"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from viajes.views import AltaReserva, mostrar_reserva, BuscarReserva
from vuelos.views import AltaVuelo, mostrar_vuelos, BuscarVuelo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservas/', mostrar_reserva),
    path('buscar-reserva', BuscarReserva.as_view()),
    path('reservar/',AltaReserva.as_view()),
    path('vuelos/', mostrar_vuelos),
    path('reservar-vuelo',AltaVuelo.as_view()),
    path('buscar-vuelo',BuscarVuelo.as_view()),
    path('panel-reservas/', include('panel_reservas.urls')),
    path('blog-opiniones/', include('blog_opiniones.urls')),
]