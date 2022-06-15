from django.shortcuts import render
from .models import *

# Create your views here.

# Getting all the project from db.
def all_projects(request):
	allProjects = ProjectsModel.objects.all()
	return render(request, 'Projects/projects.html', {'allProjects': allProjects})

# Getting specific project from db.
def specific_project(request, project_id):
	specific_project = ProjectsModel.objects.get(id=project_id)
	return render(request, 'Projects/specificProject.html', {'specific_project': specific_project})