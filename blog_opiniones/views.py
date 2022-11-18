from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from blog_opiniones.models import Opinion
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def index(request):
    opiniones = Opinion.objects.order_by("-fecha_publicacion")
    return render(request, 'blog_opiniones/index.html')

def about(request):
    return render(request, 'blog_opiniones/about.html')

class ListaOpinion(ListView):
    model = Opinion

class CrearOpinion(LoginRequiredMixin,CreateView):
    model = Opinion
    fields = ["titulo", "breve_opinion", "opinion_detallada", "firma", "imagen"]
    success_url = reverse_lazy("opiniones")

class OpinionDetallada(DetailView):
    model = Opinion

class ActualizarOpinion(LoginRequiredMixin,UpdateView):
    model = Opinion
    fields = ["titulo", "breve_opinion", "opinion_detallada", "firma", "imagen"]
    success_url = reverse_lazy("opiniones")

class BorrarOpinion(LoginRequiredMixin,DeleteView):
    model = Opinion
    success_url = reverse_lazy("opiniones")

class BuscarOpinionNombre(ListView):
    def get_queryset(self):
       opinion_titulo = self.request.GET.get("opinion-titulo")
       return Opinion.objects.filter(titulo__icontains=opinion_titulo)

class BlogLogin(LoginView):
    template_name = "blog_opiniones/blog_login.html"
    next_page = reverse_lazy("opiniones")

class BlogLogout(LogoutView):
    template_name = "blog_opiniones/blog_logout"

class BlogSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("blog-login")
    template_name = "registration/signup.html"

class ProfileUpdate(UpdateView):
    model = User
    fields = ['username', 'nombre', 'apellido', 'email']