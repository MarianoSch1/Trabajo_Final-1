
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from viajes.views import AltaReserva, mostrar_reserva, BuscarReserva, ReservaDelete
from vuelos.views import AltaVuelo, mostrar_vuelos, BuscarVuelo, VuelosDelete
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservas/', mostrar_reserva, name = "reservas"),
    path('buscar-reserva', BuscarReserva.as_view(), name= "buscar-reserva"),
    path('reservar/',AltaReserva.as_view(), name = "reservar"),
    path('vuelos/', mostrar_vuelos, name = "vuelos"),
    path('reservar-vuelo',AltaVuelo.as_view(), name = "reservar-vuelo"),
    path('buscar-vuelo',BuscarVuelo.as_view(), name= "buscar-vuelo") ,
    path('blog-opiniones/', include('blog_opiniones.urls')),
    path('<int:pk>/borrar',ReservaDelete.as_view(), name = "reserva-borrar"),
    path('<int:pk>/cancelar', VuelosDelete.as_view(), name= "vuelo-borrar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)