from django.http import HttpResponse
from django.template.loader import get_template


class urlsView():

    def index(self):
        navbar = get_template("Index.html")
        return HttpResponse(navbar.render())