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

from Views.urlView import urlsView
from Models.Alumno.views import formularioAlumnoView
from Models.Inscripcion.views import formularioInscribirView, formNotasView
from Models.Contrato.views import formularioProfesorView
from Models.Nivel.views import formGrado, formNivel
from django.urls import path
from Models.Usuario import views
from Models.Inscripcion.models import Inscripcion

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", views.LoginView.as_view(), name="login"),
    path("index", urlsView.mainView, name="index"),

    #modulo alumno y asignacion de curso
    path("registroAlumno/", formularioAlumnoView.index, name="registrarAlumno"),
    path("guardarAlumno/", formularioAlumnoView.procesarFormulario, name="guardarAlumno"),
    path("formInscribirAlumno/", formularioInscribirView.indexInscripcion, name="inscribirAlumno"),
    path("inscribirAlumno/", formularioInscribirView.formulario_Inscripcion, name="inscribir"),
    path("alumnosInscritos/", formularioInscribirView.listar_alumnos, name="mostrarInscritos"),
    path("botonEliminar/<id>/", formularioInscribirView.eliminarAlumno, name="btnEliminar"),
    path("modificarAsignacion/<id>/", formularioInscribirView.modificar_alumno_sucursal, name="modificarAsignacion"),

    #modulo profesor
    path("nuevoProfesor/", formularioProfesorView.indexProfesor , name="formProfesor"),
    path("guardarProfesor/", formularioProfesorView.formulario_Profesor, name="guardarProfesor"),
    path("asignacionCursoProfesor/", formularioProfesorView.indexAsignacionProfesor , name="formAsigProfe"),
    path("guardarAsigProfesor/", formularioProfesorView.formulario_Asignacion_Profesor, name="guardarAsigCurso"),
    path("listProfesores/", formularioProfesorView.listar_profesores, name="mostrarProfesores"),
    path("eliminarProfesor/<id>/", formularioProfesorView.eliminarProfesor, name="purgarProfesor"),
    path("modificarAsigProfesor/<id>/", formularioProfesorView.modificar_profesor, name="modificarProfesor"),

    #modulo de notas
    path("nuevaNota/", formNotasView.indexNotas, name="formNotas"),
    path("guardarNota/", formNotasView.formularioNotas, name="guardarNotas"),
    path("listNotas/", formNotasView.listar_notas, name="mostrarNotas"),
    path("eliminarNota/<id>/", formNotasView.eliminarNota, name="purgarNota"),
    # parte de enrique
    path('auth/registro/', views.SignupView.as_view(), name='signup'),
    path('auth/', views.Dashboard, name='dashboard'),
    path('auth/logout/', views.Logout, name='logout'),
    # grado
    path("nuevoGrado/", formGrado.new, name="newGrade"),
    path("guardarGrado/", formGrado.save, name="saveGrade"),
    path("listGrados/", formGrado.index, name="indexGrade"),
    path("eliminarGrado/<id>/", formGrado.delete, name="deleteGrade"),
    # nivel
    path("nuevoNivel/", formNivel.new, name="newLevel"),
    path("guardarNivel/", formNivel.save, name="saveLevel"),
    path("listNivel/", formNivel.index, name="indexLevel"),
    path("eliminarNivel/<id>/", formNivel.delete, name="deleteLevel"),
]

