
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from viajes.views import AltaReserva, mostrar_reserva, BuscarReserva, ReservaDelete, ReservaUpdate
from vuelos.views import AltaVuelo, mostrar_vuelos, BuscarVuelo
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservas/', mostrar_reserva, name = "reservas"),
    path('buscar-reserva', BuscarReserva.as_view()),
    path('reservar/',AltaReserva.as_view(), name = "reservar"),
    path('vuelos/', mostrar_vuelos, name = "vuelos"),
    path('reservar-vuelo',AltaVuelo.as_view(), name = "reservar-vuelo"),
    path('buscar-vuelo',BuscarVuelo.as_view()),
    path('blog-opiniones/', include('blog_opiniones.urls')),
    path('<int:pk>/borrar',ReservaDelete.as_view(), name = "reserva-borrar"),
    path('<int:pk>/actualizar',ReservaUpdate.as_view(), name = "reserva-actualizar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)