# Importing render to render the html page.
# Importing redirect to redirect the user to the specific page.
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Importing messages.
from django.contrib import messages

from Users.features import pagination

# Importing forms and models of the project.
from .forms import *
from .models import *
from django.db.models import Q

# Create your views here.
# Getting all the project from db.
def all_projects(request):

	# Search projects.
	search = ''

	if request.GET.get('search'):
		search = request.GET.get('search')
	
	# Get projects depending on the search.
	allProjects = ProjectsModel.objects.distinct().filter(
		Q(project_title__icontains=search) 
	| Q(project_description__icontains=search) 
	| Q(project_skills__name__icontains=search) 
	| Q(project_owner__first_name__icontains=search) 
	| Q(project_owner__last_name__icontains=search)).order_by('-vote_ratio', '-total_votes', '-project_title')

	# Pagination.
	# Passing an array of objects and the number of objects per page.

	projects, custom_range, p, page = pagination(request, allProjects)

	# Render searched projects to the html page.
	return render(request, 'Projects/GetProjects/projects.html', {
		'allProjects': projects,
		'page': int(page), 
		'search': search, 
		'p': p, 
		'custom_range': custom_range
	})

# Getting specific project from db.
def specific_project(request, project_id):
	# Get all the project from db depend on the project_id.
	specific_project = ProjectsModel.objects.get(id=project_id)

	# If user is logged in then get the user profile.
	if request.user.is_authenticated == True:
		profile = UserProfileModel.objects.get(user=request.user)

	# Get all the reviews of the project.
	all_reviews = ProjectReviewModel.objects.filter(project=specific_project)

	review_owners = []

	# append all reviews owner id to review_owners.
	for review in all_reviews:
		review_owners.append(review.reviewer.id)
		
	# Get the form to submit the review.
	if request.user.is_authenticated == False:
		form = ReviewForm(None, specific_project)
	else:
		form = ReviewForm(profile, specific_project)

	if request.method == 'POST':
		form = ReviewForm(profile, specific_project, request.POST)

		# If user want to submit review again, then prompt them they have already submitted a review.
		if form.non_field_errors():
			messages.error(request, form.non_field_errors())
			return redirect('specific_project', str(project_id))

		# If form is valid then save the review.
		if form.is_valid():
			form.save()
			messages.success(request, 'Review submitted successfully.')
			return redirect('specific_project', str(project_id))
		else:
			# If form is invalid then prompt the user to fill the form correctly.
			for error in form.errors:
				messages.error(request, error)
				return redirect('specific_project', str(project_id))

	# Render the specific review to the html page.
	if request.user.is_authenticated == True:
		return render(request, 'Projects/GetProjects/specificProject.html', {
			'specific_project': specific_project, 
			'form': form,
			'review_owners': review_owners, 
			'profile': profile
			})
	else:
		return render(request, 'Projects/GetProjects/specificProject.html', {
			'specific_project': specific_project, 
			'form': form,
			'review_owners': review_owners
			})

# Create a new Project.
# Project creating required user to login. and redirect to login page.
@login_required(login_url='user_login')
def create_project(request):
	# Get the ProjectForm. 
	user_profile = UserProfileModel.objects.get(user=request.user)

	form = ProjectForm(user_profile)

	# If form is submitted then check form is valid or not.
	if request.method == 'POST':
		# request.FILES to get the image.
		form = ProjectForm(user_profile, request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('user_account')
		else:
			# If form is not valid then render the form with error messages.
			for field in form.errors:
				messages.error(request, field)
			
			return redirect('create_project')

	# Otherwise render the empty form.
	return render(request, 'Projects/ProjectForm/projectForm.html', {'form': form, 'create': True})

# Update an Existing Project.
# Project updating required user to login. and redirect to login page.
@login_required(login_url='user_login')
def update_project(request, project_id):
	# Get the specific project from db to update depend on project_id.
	project = ProjectsModel.objects.get(id=project_id)

	user_profile = UserProfileModel.objects.get(user=request.user)

	if project.project_owner == user_profile:
		pass
	else:
		messages.error(request, 'You are not allowed to update this project.')
		return redirect('projects')
	
	# Get the ProjectForm. So, all the inputs have to be filled.
	form = ProjectForm(user_profile, initial={
		'project_image': None,
	},instance=project)

	if request.method == 'POST':
		# request.FILES to get the image. and instance=project to update the project.
		form = ProjectForm(user_profile, request.POST, request.FILES, instance=project, initial={
			'project_image': None,
		})
		# If form is valid then save the form. and Project updated.
		# Redirect to all the projects page.
		if form.is_valid():
			form.save()
			return redirect('user_account')
		else:
			# If form is not valid then render the form with error messages.
			for field in form.errors:
				messages.error(request, field)
			
			return redirect('update_project', project_id)
	
	# Otherwise render the empty form.
	return render(request, 'Projects/ProjectForm/projectForm.html', {'form': form, 'create': False})

# Delete an Existing Project.
# Project delete required user to login. and redirect to login page.
@login_required(login_url='user_login')
def delete_project_confirmation(request, project_id):
	# Get the specific project from db to delete depend on project_id.
	project = ProjectsModel.objects.get(id=project_id)

	user_profile = UserProfileModel.objects.get(user=request.user)

	if project.project_owner == user_profile:
		pass
	else:
		messages.error(request, 'You are not allowed to delete this project.')
		return redirect('user_account')

	# If POST request has been submitted then delete the project and redirect to all the projects page.
	if request.method == 'POST':
		project.delete()
		return redirect('user_account')

	# Otherwise render the delete confirmation page.
	return render(request, 'Projects/ConfirmationPage/deleteTemplate.html', {'project': project})