from django.shortcuts import render

from .models import *
from UserProjects.models import *

# Create your views here.

def allUsers(request):
	users = UserProfileModel.objects.all()
	return render(request, 'Users/Home/allUsers.html', {'users': users})

def user_profile(request, user_id):
	user = UserProfileModel.objects.get(id=user_id)
	projects = ProjectsModel.objects.filter(project_owner=user_id)
	topSkills = user.skills.exclude(description__exact=None)
	otherSkills = user.skills.filter(description=None)
	
	return render(request, 'Users/UserProfile/userProfile.html', {'user': user, 'projects': projects, 'topSkills': topSkills, 'otherSkills': otherSkills})
