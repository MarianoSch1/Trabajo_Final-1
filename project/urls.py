
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from viajes.views import AltaReserva, mostrar_reserva, BuscarReserva
from vuelos.views import AltaVuelo, mostrar_vuelos, BuscarVuelo
from django.conf.urls.static import static

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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)