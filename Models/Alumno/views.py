from django.http import HttpRequest
from django.shortcuts import render, redirect
from Models.Alumno.forms import formularioNuevoAlumno
from Models.Alumno.models import Alumno



class formularioAlumnoView(HttpRequest):

    def index(request):

        alumno = formularioNuevoAlumno()
        return render(request, 'nuevoAlumno.html', {'form':alumno})

    def procesarFormulario(request):

        alumno = formularioNuevoAlumno(request.POST)
        if alumno.is_valid():
            alumno.save()
            alumno = formularioNuevoAlumno()
        return render(request, "nuevoAlumno.html", {"form":alumno, "mensaje": "ok"})

    def listar_registrados(request):
        alumno = Alumno.objects.all()
        return render(request, "listAlumno.html", {"lb_alumnos": alumno})
