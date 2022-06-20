# Importing render to render the html page.
# Importing redirect to redirect the user to the specific page.
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Importing forms and models of the project.
from .forms import *
from .models import *

# Create your views here.

# Getting all the project from db.
def all_projects(request):
	# Get all the project of db.
	allProjects = ProjectsModel.objects.all()

	# Render all the projects to the html page.
	return render(request, 'Projects/GetProjects/projects.html', {'allProjects': allProjects})

# Getting specific project from db.
def specific_project(request, project_id):
	# Get all the project from db depend on the project_id.
	specific_project = ProjectsModel.objects.get(id=project_id)

	# Render the specific project to the html page.
	return render(request, 'Projects/GetProjects/specificProject.html', {'specific_project': specific_project})

# Create a new Project.
# Project creating required user to login. and redirect to login page.
@login_required(login_url='user_login')
def create_project(request):
	# Get the ProjectForm. 
	form = ProjectForm()

	# If form is submitted then check form is valid or not.
	if request.method == 'POST':
		# request.FILES to get the image.
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			# If form is valid then save the form. and Project created.
			# Redirect to all the projects page.
			form.save()
			return redirect('projects')

	# Otherwise render the empty form.
	return render(request, 'Projects/ProjectForm/projectForm.html', {'form': form, 'create': True})

# Update an Existing Project.
# Project updating required user to login. and redirect to login page.
@login_required(login_url='user_login')
def update_project(request, project_id):
	# Get the specific project from db to update depend on project_id.
	project = ProjectsModel.objects.get(id=project_id)
	# Get the ProjectForm. So, all the inputs have to be filled.
	form = ProjectForm(initial={
		'project_image': None,
	},instance=project)

	if request.method == 'POST':
		# request.FILES to get the image. and instance=project to update the project.
		form = ProjectForm(request.POST, request.FILES, instance=project)
		# If form is valid then save the form. and Project updated.
		# Redirect to all the projects page.
		if form.is_valid():
			form.save()
			return redirect('projects')
	
	# Otherwise render the empty form.
	return render(request, 'Projects/ProjectForm/projectForm.html', {'form': form, 'create': False})

# Delete an Existing Project.
# Project delete required user to login. and redirect to login page.
@login_required(login_url='user_login')
def delete_project_confirmation(request, project_id):
	# Get the specific project from db to delete depend on project_id.
	project = ProjectsModel.objects.get(id=project_id)

	# If POST request has been submitted then delete the project and redirect to all the projects page.
	if request.method == 'POST':
		project.delete()
		return redirect('projects')

	# Otherwise render the delete confirmation page.
	return render(request, 'Projects/ConfirmationPage/deleteTemplate.html', {'project': project})