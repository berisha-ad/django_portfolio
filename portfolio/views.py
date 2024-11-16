from django.shortcuts import render
from .models import Project, Backend, Frontend, Tools, Files



# Create your views here.
def index(request):
    backend = Backend.objects.all()
    frontend = Frontend.objects.all()
    tools = Tools.objects.all()
    files = Files.objects.first()
    return render(request, "portfolio/index.html", {
        "backend" : backend,
        "frontend": frontend,
        "tools": tools,
        "files": files
    })

def projects(request):
    projects = Project.objects.all()
    files = Files.objects.first()
    return render(request, "portfolio/projects.html", {
        "projects" : projects,
        "files" : files
    })

def imprint(request):
    files = Files.objects.first()
    return render(request, "portfolio/imprint.html", {
        "files" : files
    })

