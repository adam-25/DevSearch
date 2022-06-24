from django.shortcuts import redirect, render

# Importing login, logout, authenticate to do User authentication and authorization stuff.
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .features import pagination

# App models and Projects app Model.
from .models import *
from UserProjects.models import *
from django.db.models import Q

# Importing SignUpForm from forms.
from .forms import *

# Create your views here.

# All the users in DB.
def allUsers(request):

	search = '';

	if request.GET.get('search'):
		search = request.GET.get('search')

	# Filter project by search when search contains either first_name, last_name, profession or skills.
	users = UserProfileModel.objects.distinct().filter(
		Q(first_name__icontains=search) 
		| Q(last_name__icontains=search) 
		| Q(skills__name__icontains=search) 
		| Q(profession__icontains=search))

	# Pagination
	users, custom_range, p, page = pagination(request, users)

	# Return template with users with specific search.
	return render(request, 'Users/Home/allUsers.html', {
		'users': users, 
		'search': search, 
		'custom_range': custom_range, 
		'p': p, 
		'page': int(page)
	})

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
			return redirect('edit_account')
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

# User can edit their account.
@login_required(login_url='user_login')
def edit_account_profile(request):

	# Getting user profile.
	profile = UserProfileModel.objects.get(user=request.user)

	form = EditHeadlineForm(initial={
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

	# Getting all users.
	all_user_profile = UserProfileModel.objects.all()

	usernames = []

	# Append all the usernames to the usernames list.
	for user in all_user_profile:
		usernames.append(user.username)
	
	# remove current user name from the list.
	usernames.remove(profile.username)

	if request.method == 'POST':
		form = EditHeadlineForm(request.POST, request.FILES, instance=profile)

		# If username already exist in the database then display a message.
		if request.POST['username'] in usernames:
			messages.error(request, "Username already exists.")
			redirect('edit_account')		
		else:
			# If form is valid then save the form.
			if form.is_valid():
				form.save()
				messages.success(request, "User has been updated successfully")
				return redirect('user_account')
			else:
				for field in form.errors:
					messages.error(request, field)
				
				return redirect('edit_account')

	return render(request, 'Users/UserProfile/EditProfile/editHeadlines.html', {'form': form})

# Add skill which have an description.
@login_required(login_url='user_login')
def add_top_skill(request):

	# Getting user profile.
	profile = UserProfileModel.objects.get(user=request.user)

	# Getting all the skills associated with the user.
	allSkills = SkillsModel.objects.filter(owner=profile)

	skills = []

	# Append all the skills to the skills list.
	for i in allSkills:
		skills.append(i.name)

	# Get the form to add a skill.
	form = AddSkillForm(profile)

	if request.method == 'POST':
		form = AddSkillForm(profile, request.POST)

		# If skill already exist with an owner then display a message.
		if request.POST['name'] in skills:
			messages.error(request, "Skill already exists.")
			return redirect('add_top_skill')

		# If form is valid then save the form.
		if form.is_valid():
			form.save()
			messages.success(request, "Skill has been added successfully")
			return redirect('user_account')
		else:
			for field in form.errors:
				messages.error(request, field)
			
			return redirect('add_top_skill')

	return render(request, 'Users/UserProfile/EditProfile/addSkills.html', {'form': form})


# Add skill which does not have a description.
@login_required(login_url='user_login')
def add_other_skill(request):

	# Getting user profile and skill associated with it.
	profile = UserProfileModel.objects.get(user=request.user)
	allSkills = SkillsModel.objects.filter(owner=profile)

	skills = []

	# Append all the skills to the skills list.
	for i in allSkills:
		skills.append(i.name)

	# Get the form to add a skill.
	form = AddOtherSkillForm(profile)

	if request.method == 'POST':
		form = AddOtherSkillForm(profile, request.POST)

		# If skill already exist with an owner then display a message.
		if request.POST['name'] in skills:
			messages.error(request, "Skill already exists.")
			return redirect('add_other_skill')

		# If form is valid then save the form.
		if form.is_valid():
			form.save()
			messages.success(request, "Skill has been added successfully")
			return redirect('user_account')
		else:
			for field in form.errors:
				messages.error(request, field)
			
			return redirect('add_top_skill')

	return render(request, 'Users/UserProfile/EditProfile/addSkills.html', {'form': form})

# Edit skill which have a description.
@login_required(login_url='user_login')
def edit_top_skill(request, skill_id):
	
	# Getting skill, profile.
	skill = SkillsModel.objects.get(id=skill_id)
	profile = UserProfileModel.objects.get(user=request.user)
	allSkills = SkillsModel.objects.filter(owner=profile)
	skills = []

	# Append all the skills to the skills list.
	for i in allSkills:
		skills.append(i.name)

	form = AddOtherSkillForm(profile)

	# If skill owner is not the current user then display a message.
	if skill.owner.id != profile.id:
		messages.error(request, "You are not allowed to edit this skill.")
		return redirect('user_account')
	
	form = AddSkillForm(profile, instance=skill)

	if request.method == 'POST':
		form = AddSkillForm(profile, request.POST, instance=skill)

		# If skill already exist with an owner then display a message.
		if request.POST['name'] in skills and request.POST['name'] != skill.name:
			messages.error(request, "Skill already exists.")
			return redirect('edit_top_skill', skill_id=skill_id)

		# If form is valid then save the form.
		if form.is_valid():
			form.save()
			messages.success(request, "Skill has been updated successfully")
			return redirect('user_account')
		else:
			for field in form.errors:
				messages.error(request, field)
			
			return redirect('edit_top_skill', skill_id)

	return render(request, 'Users/UserProfile/EditProfile/addSkills.html', {'form': form, 'edit': True})

# Edit skill which does not have a description.
@login_required(login_url='user_login')
def edit_other_skill(request, skill_id):

	# Getting skill, profile.
	skill = SkillsModel.objects.get(id=skill_id)
	profile = UserProfileModel.objects.get(user=request.user)

	# If skill owner is not the current user then display a message.
	if skill.owner.id != profile.id:
		messages.error(request, "You are not allowed to edit this skill.")
		return redirect('user_account')

	# Get all skill associated with the user.
	allSkills = SkillsModel.objects.filter(owner=profile)
	skills = []

	for i in allSkills:
		skills.append(i.name)

	form = AddOtherSkillForm(profile, instance=skill)

	if request.method == 'POST':
		form = AddOtherSkillForm(profile, request.POST, instance=skill)

		# If skill already exist with an owner then display a message.
		if request.POST['name'] in skills and request.POST['name'] != skill.name:
			messages.error(request, "Skill already exists.")
			return redirect('edit_other_skill', skill_id=skill_id)

		# If form is valid then save the form.
		if form.is_valid():
			form.save()
			messages.success(request, "Skill has been updated successfully")
			return redirect('user_account')
		else:
			for field in form.errors:
				messages.error(request, field)
			
			return redirect('edit_other_skill', skill_id)


	return render(request, 'Users/UserProfile/EditProfile/addSkills.html', {'form': form, 'otherSkill': True, 'skill_id': skill_id, 'edit': True})

# Delete skill.
@login_required(login_url='user_login')
def delete_skill(request, skill_id):

	# Get skill and profile.
	skill = SkillsModel.objects.get(id=skill_id)
	user_profile = UserProfileModel.objects.get(user=request.user)

	# If skill owner is not the current user then display a message.
	if skill.owner.id != user_profile.id:
		messages.error(request, 'You are not allowed to delete this skill.')
		return redirect('user_account')

	# Delete skill.
	if request.method == 'POST':
		skill.delete()
		return redirect('user_account')
	else:
		return render(request, 'Projects/ConfirmationPage/deleteTemplate.html', {'project': skill})