from django.http import HttpRequest
from django.shortcuts import render, redirect
from Models.Inscripcion.forms import formularioInscripcion
from Models.Inscripcion.forms import Inscripcion


class formularioInscribirView(HttpRequest):

    def indexInscripcion(request):

        inscribir = formularioInscripcion()
        return render(request, 'inscribirAlumno.html', {'form':inscribir})

    def formularioInscripcion(request):

        inscripcion = formularioInscripcion(request.POST)
        if inscripcion.is_valid():
            inscripcion.save()
            inscripcion = formularioInscripcion()

        return render(request, "inscribirAlumno.html", {"form":inscripcion, "mensaje": "ok"})

    def listar_alumnos(request):
        alumnos = Inscripcion.objects.all()
        return render(request, "listAlumnoInscrito.html", {"lb_alumnos": alumnos})

    def eliminarAlumno(request, id):
        Inscripcion.objects.filter(id_inscripcion=id).delete()


        return redirect(to="mostrarInscritos")