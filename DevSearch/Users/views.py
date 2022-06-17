from django.shortcuts import render

from .models import *

# Create your views here.

def allUsers(request):
	users = UserProfileModel.objects.all()
	return render(request, 'Users/Home/allUsers.html', {'users': users})