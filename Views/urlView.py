from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render


class urlsView():

    def index(self, request):
        navbar = get_template("Index.html")
        return HttpResponse(request, navbar.render())


def mainView(request):
    return render(request, 'Index.html')
