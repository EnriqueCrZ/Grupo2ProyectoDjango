"""Desweb2020Grupo2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path
from Views.urlView import urlsView
from Models.Alumno.views import formularioAlumnoView
from Models.Inscripcion.views import formularioInscribirView
from django.urls import path, include
from Models.Usuario import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", urlsView.index, name="navbar"),
    path("registroAlumno/", formularioAlumnoView.index, name="registrarAlumno"),
    path("guardarAlumno/", formularioAlumnoView.procesarFormulario, name="guardarAlumno"),
    path("formInscribirAlumni", formularioInscribirView.indexInscripcion, name="inscribirAlumno"),
    path("inscribirAlumno/", formularioInscribirView.formularioInscripcion, name="inscribir"),
    path("alumnosInscritos/", formularioInscribirView.listar_alumnos, name="mostrarInscritos"),
    path("botonEliminar/<int:id>/", formularioInscribirView.eliminarAlumno, name="btnEliminar"),

    # parte de enrique
    path('auth/registro/', views.SignupView.as_view(), name='signup'),
    path('auth/', views.Dashboard, name='dashboard'),
    path('auth/logout/', views.Logout, name='logout'),
    path('auth/login/', views.LoginView.as_view(), name='login'),

]