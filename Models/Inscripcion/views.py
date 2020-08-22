from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render, redirect
from Models.Inscripcion.forms import formularioInscripcion, formularioNota
from Models.Inscripcion.forms import Inscripcion, Nota
from Models.Nivel.forms import Nivel
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

    #metodos de reporte

class reporInscritosView(HttpRequest): #view de opciones de reporte


    def indexReportInscritos(request):


        return render(request, 'reportes.html')

    # Reporte de inscritos por fecha
    def reportInscritos(request):
        qs = Inscripcion.objects.all()

        date_min = request.GET.get('date_min')
        date_max= request.GET.get('date_max')


        if date_min != '' and date_min is not None:
            qs = qs.filter(fecha__gte=date_min)

        if date_max != '' and date_max is not None:
            qs = qs.filter(fecha__lte=date_max)


        return render(request, "reportInscritos.html", {'queryset': qs})

    # Reporte de inscritos por grado y curso


    def reportInscritos_cursoYgrado(request):
        qs = Inscripcion.objects.all()
        grado_seccion = Nivel.objects.all()

        category = request.GET.get('category')

        if category != '' and category is not None and category != 'Seleccion':

            if category == 'Novato Principiantes1':

                variable = 1
                qs = qs.filter(nivel_id_nivel_id__exact=variable)

            elif category == 'Novato Principiantes2':

                variable = 2
                qs = qs.filter(nivel_id_nivel_id__exact=variable)

            elif category == 'Experto Avanzados1':

                variable = 3
                qs = qs.filter(nivel_id_nivel_id__exact=variable)
            elif category == 'Experto Avanzados2':

                variable = 4
                qs = qs.filter(nivel_id_nivel_id__exact=variable)

        context = {
            'queryset': qs,
            'seccion_grado': grado_seccion
        }
        return render(request, 'reportInscritosCurso_Grado.html', context)

    #reporte por alumno de nota

    def reportAlumnoNota(request):
        qs = Nota.objects.all()

        alumno = request.GET.get('title_contains')

        if alumno != '' and alumno is not None:
            qs = qs.filter(inscripcion_id_inscripcion__alumno_id_alumno__nombre__contains=alumno)

        context = {

            'queryset': qs

        }

        return render(request, 'reportNotas.html', context )
