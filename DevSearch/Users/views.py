# Redirect page.
from django.shortcuts import redirect, render

# Importing login, logout, authenticate to do User authentication and authorization stuff.
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# App models and Projects app Model.
from .models import *
from UserProjects.models import *

# Importing SignUpForm from forms.
from .forms import *

# Create your views here.

# All the users in DB.
def allUsers(request):
	# Request all the users.
	users = UserProfileModel.objects.all()

	# Return allUsers template with users.
	return render(request, 'Users/Home/allUsers.html', {'users': users})

# Get specific user and render it.
def userProfile(request, user_id):
	# Get user from db by id.
	user = UserProfileModel.objects.get(id=user_id)
	# Get all the projects of the user.
	projects = ProjectsModel.objects.filter(project_owner=user_id)

	# Getting skills with the description is not None. Exclude those skills.
	topSkills = user.skills.exclude(description__exact='')
	# Get other skills of user which description is None.
	otherSkills = user.skills.filter(description='')
	
	# Render html page of specific user depend on the user id.
	return render(request, 'Users/UserProfile/userProfile.html', {'user': user, 'projects': projects, 'topSkills': topSkills, 'otherSkills': otherSkills})

# Login user.
def loginUser(request):

	# Check if the user is authenticated then do not show login page and redirect it to the home page.
	if request.user.is_authenticated:
		return redirect('/')

	# If user make a 'POST' request to login then login the user depend on the credentials.
	if request.method == 'POST':
		# Get username and password from the form.
		username = request.POST['username']
		password = request.POST['password']

		# Get the user from database.
		# If there is not user then redirect back to the login page.
		try:
			user = User.objects.get(username=username)
		except:
			messages.error(request, 'Invalid username or password.')
			return redirect('user_login')

		# Check username and password is correct or not..
		user = authenticate(request, username=username, password=password)

		# If user name and password is correct then login the user and redirect it to the home page.
		# otherwise redirect back to the login page.
		if user != None:
			login(request, user)
			return redirect('/')
		else:
			messages.error(request, 'Invalid username or password.')
			return redirect('user_login')
	
	# If user is authenticated and didn't make a post request then show login page.
	return render(request, 'Users/LoginRegister/loginRegister.html', {'login': True})

# Logout user.
def logoutUser(request):
	# Logout user and redirect to the home page.
	logout(request)
	return redirect('/')

# Registering User.
def registerUser(request):
	# If user is already logged in then they cannot access this route.
	if request.user.is_authenticated:
		return redirect('/')

	# SignUpForm.
	form = SignUpForm()

	# If there is a post request, then User check user form is valid or not.
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		# If user submitted information is valid then save the form(user). 
		# Then authenticate and login the user and redirect to home page.
		if form.is_valid():
			form.save()
			user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password2'])
			login(request, user)
			messages.success(request, "User account has been created successfully...")
			return redirect('/')
		else:
			# If there is an error in form, Display a message of an error.
			for i in form.errors.values():
				messages.error(request, i)
			
			# Redirect to registration page.
			return redirect('user_register')

	# Render an empty form for registration.
	return render(request, 'Users/LoginRegister/loginRegister.html', {'login': False, 'form': form})

# User can view their account.
# It required user to logged in, if user is not logged in then redirect user to the login page.
@login_required(login_url='user_login')
def user_account(request):
	# Getting user profile.
	userProfile = UserProfileModel.objects.get(user=request.user)

	# Getting user projects.
	projects = ProjectsModel.objects.filter(project_owner=userProfile)

	# Skills of an user.
	topSkills = userProfile.skills.exclude(description__exact='')
	otherSkills = userProfile.skills.filter(description='')

	# Render html page and passing users skills and projects.
	return render(request, 'Users/UserProfile/userAccount.html', {'user': userProfile, 'topSkills': topSkills, 'projects': projects, 'otherSkills': otherSkills})

@login_required(login_url='user_login')
def edit_account_profile(request):

	profile = UserProfileModel.objects.get(user=request.user)

	form = EditHeadlineForm(request.user, initial={
		'first_name': profile.first_name,
		'last_name': profile.last_name,
		'username': profile.username,
		'user_email': profile.user_email,
		'profession': profile.profession,
		'location': profile.location,
		'bio': profile.bio,
		'github': profile.github,
		'linkedin': profile.linkedin,
		'twitter': profile.twitter,
		'youtube': profile.youtube,
		'website': profile.website,
		'image': None
	}, instance=profile)

	all_user_profile = UserProfileModel.objects.all()

	usernames = []

	for user in all_user_profile:
		usernames.append(user.username)
	
	usernames.remove(profile.username)

	if request.method == 'POST':
		form = EditHeadlineForm(request.POST, request.FILES, instance=profile)

		if request.POST['username'] in usernames:
			messages.error(request, "Username already exists.")
			redirect('edit_account')		
		else:
			if form.is_valid():
				form.save()
				messages.success(request, "User has been updated successfully")
				return redirect('user_account')
			else:
				for field in form.errors:
					messages.error(request, field)
				
				return redirect('edit_account')

	return render(request, 'Users/UserProfile/EditProfile/editHeadlines.html', {'form': form})