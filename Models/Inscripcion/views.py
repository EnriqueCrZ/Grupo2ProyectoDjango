from django.http import HttpRequest
from django.shortcuts import render, redirect
from Models.Inscripcion.forms import formularioInscripcion
from Models.Inscripcion.forms import Inscripcion


class formularioInscribirView(HttpRequest):

    def indexInscripcion(request):

        inscribir = formularioInscripcion()
        return render(request, 'inscribirAlumno.html', {'form':inscribir})

    def formulario_Inscripcion(request):

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

#    def modificar_alumno_sucursal(request, id):

 #       alumno_sucursal = Inscripcion.objects.get(id_inscripcion=id)
  #      data = { 'form': formularioInscripcion(instance=alumno_sucursal)}

   #     return render(request, 'modificar_inscripcion.html', data)

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