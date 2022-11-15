from django.urls import path
from panel_reservas.views import ReservaList, ReservaCrear, ReservaDelete, ReservaUpdate

urlpatterns = [
    path('',ReservaList.as_view(), name = "reserva-lista"),
    path('crear', ReservaCrear.as_view(), name = "reserva-crear"),
    path('<int:pk>/borrar',ReservaDelete.as_view(), name = "reserva-borrar"),
    path('<int:pk>/actualizar',ReservaUpdate.as_view(), name = "reserva-actualizar"),
]