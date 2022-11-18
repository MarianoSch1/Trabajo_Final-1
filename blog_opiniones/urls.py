from django.urls import path
from blog_opiniones.views import *

urlpatterns = [
    path('',index, name="index-blog"),
    path('opiniones/', ListaOpinion.as_view(), name="opiniones"),
    path('crear-opinion/', CrearOpinion.as_view(), name="crear-opinion"),
    path('opinion-detallada/<int:pk>/', OpinionDetallada.as_view(), name="opinion-detallada"),
    path('actualizar-opinion/<int:pk>/', ActualizarOpinion.as_view(), name="actualizar-opinion"),
    path('borrar-opinion/<int:pk>/', BorrarOpinion.as_view(), name="borrar-opinion"),
    path('buscar-titulo/', BuscarOpinionNombre.as_view(), name="buscar-titulo"),
    path('login/', BlogLogin.as_view(), name="blog-login"),
    path('logout/', BlogLogout.as_view(), name="blog-logout"),
    path('signup/', BlogSignUp.as_view(), name="blog-signup"),
    path('user-profile/<int:pk>', ProfileUpdate.as_view(), name="profile-update"),
    path('about/',about, name="about"),
]

