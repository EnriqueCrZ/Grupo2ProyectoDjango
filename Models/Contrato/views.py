from django.shortcuts import render, redirect
from django.http import HttpRequest
from Models.Contrato.forms import formioNuevoCatedratico, formContrato, Contrato


class formularioProfesorView(HttpRequest):

    #ingreso de nuevo profesor
    def indexProfesor(request):

        profesor = formioNuevoCatedratico()
        return render(request, 'nuevoProfesor.html', {'form': profesor})

    def formulario_Profesor(request):

        prof = formioNuevoCatedratico(request.POST)
        if prof.is_valid():
            prof.save()
            prof = formioNuevoCatedratico()
        return render(request, "nuevoProfesor.html", {"form":prof, "mensaje": "ok"})

    #asignacion de curso al profesor
    def indexAsignacionProfesor(request):

        profesor = formContrato()
        return render(request, 'asignarProfesor.html', {'form': profesor})

    def formulario_Asignacion_Profesor(request):

        profe = formContrato(request.POST)
        if profe.is_valid():
            profe.save()
            profe = formContrato()
        return render(request, "asignarProfesor.html", {"form":profe, "mensaje": "ok"})

    #listado de profesores asignados
    def listar_profesores(request):
        profes = Contrato.objects.all()
        return render(request, "listProfesores.html", {"lb_Profesores": profes})

    #eliminar profesor ya asignado

    def eliminarProfesor(request, id):
        Contrato.objects.filter(id_contrato=id).delete()


        return redirect(to="mostrarProfesores")

    #modificar asaignacion de profesor
    def modificar_profesor(request, id):
        modificarRegistro = Contrato.objects.get(id_contrato=id)
        data = {
            'form': formContrato(instance=modificarRegistro)
        }
        if request.method == 'POST':
            formulario = formContrato(data=request.POST, instance=modificarRegistro)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = "modificacion correcta"
                data['form'] = formulario
        return render(request, 'modificar_asignacion_profesor.html', data)
