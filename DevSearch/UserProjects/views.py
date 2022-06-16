from django.shortcuts import redirect, render

from .forms import ProjectForm
from .models import *

# Create your views here.

# Getting all the project from db.
def all_projects(request):
	allProjects = ProjectsModel.objects.all()
	return render(request, 'Projects/GetProjects/projects.html', {'allProjects': allProjects})

# Getting specific project from db.
def specific_project(request, project_id):
	specific_project = ProjectsModel.objects.get(id=project_id)
	return render(request, 'Projects/GetProjects/specificProject.html', {'specific_project': specific_project})

# Create a new Project.
def create_project(request):
	form = ProjectForm()

	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('projects')

	return render(request, 'Projects/ProjectForm/projectForm.html', {'form': form})

# Update an Existing Project.
def update_project(request, project_id):
	project = ProjectsModel.objects.get(id=project_id)
	form = ProjectForm(instance=project)

	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES, instance=project)
		if form.is_valid():
			form.save()
			return redirect('projects')
	
	return render(request, 'Projects/ProjectForm/projectForm.html', {'form': form})

def delete_project_confirmation(request, project_id):
	project = ProjectsModel.objects.get(id=project_id)

	if request.method == 'POST':
		project.delete()
		return redirect('projects')

	return render(request, 'Projects/ConfirmationPage/deleteTemplate.html', {'obj': project})