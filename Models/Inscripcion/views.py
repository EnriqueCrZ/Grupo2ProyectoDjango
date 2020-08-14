from django.http import HttpRequest
from django.shortcuts import render, redirect
from Models.Inscripcion.forms import formularioInscripcion, formularioNota
from Models.Inscripcion.forms import Inscripcion, Nota
import logging


class formularioInscribirView(HttpRequest):

    def indexInscripcion(request):

        inscribir = formularioInscripcion()
        return render(request, 'inscribirAlumno.html', {'form':inscribir})

    def formulario_Inscripcion(request):

        inscripcion = formularioInscripcion(request.POST)

        logger = logging.getLogger(__name__)

        if inscripcion.is_valid():
            registro = inscripcion.save(commit=False)
            registro.usuario_id_user = request.user
            logger.error(registro)
            registro.save()
            inscripcion = formularioInscripcion()

        return render(request, "inscribirAlumno.html", {"formset":inscripcion, "mensaje": "ok"})

    def listar_alumnos(request):
        alumnos = Inscripcion.objects.all()
        return render(request, "listAlumnoInscrito.html", {"lb_alumnos": alumnos})

    def eliminarAlumno(request, id):
        Inscripcion.objects.filter(id_inscripcion=id).delete()


        return redirect(to="mostrarInscritos")

    def modificar_alumno_sucursal(request, id):
        modificarRegistro = Inscripcion.objects.get(id_inscripcion=id)
        data = {
            'form': formularioInscripcion(instance=modificarRegistro)
        }
        if request.method == 'POST':
            formulario = formularioInscripcion(data=request.POST, instance=modificarRegistro)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = "modificacion correcta"
                data['form'] = formulario
        return render(request, 'modificar_inscripcion.html', data)

#formulario de notas

class formNotasView(HttpRequest):

    def indexNotas(request):
        nota = formularioNota()
        return render(request, 'nuevaNota.html', {'form': nota})

    def formularioNotas(request):
        lbNota = formularioNota(request.POST)
        if lbNota.is_valid():
            lbNota.save()
            lbNota = formularioNota()
        return render(request, "nuevaNota.html", {"form": lbNota, "mensaje": "ok"})

    def listar_notas(request):
        notas = Nota.objects.all()
        return render(request, "listNotas.html", {"lb_notas": notas})

    def eliminarNota(request, id):
        Nota.objects.filter(id_nota=id).delete()
        return redirect(to="mostrarNotas")