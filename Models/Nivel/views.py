from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import formularioGrado, Grado, formularioNivel, Nivel


class formGrado(HttpRequest):
    def new(request):
        nota = formularioGrado()
        return render(request, 'grado_nuevo.html', {'form': nota})

    def save(request):
        grado = formularioGrado(request.POST)
        if grado.is_valid():
            grado.save()
            grado = formularioGrado()
        return render(request, "grado_nuevo.html", {"form": grado, "mensaje": "ok"})

    def index(request):
        grados = Grado.objects.all()
        return render(request, "grado_index.html", {"lb_grados": grados})

    def delete(request, id):
        Grado.objects.filter(id_grado=id).delete()
        return redirect(to="indexGrade")


class formNivel(HttpRequest):
    def new(request):
        nivel = formularioNivel()
        return render(request, 'nivel_nuevo.html', {'form': nivel})

    def save(request):
        nivel = formularioGrado(request.POST)
        if nivel.is_valid():
            nivel.save()
            nivel = formularioNivel()
        return render(request, "nivel_nuevo.html", {"form": nivel, "mensaje": "ok"})

    def index(request):
        niveles = Nivel.objects.all()
        return render(request, "nivel_index.html", {"lb_niveles": niveles})

    def delete(request, id):
        Nivel.objects.filter(id_nivel=id).delete()
        return redirect(to="indexLevel")
