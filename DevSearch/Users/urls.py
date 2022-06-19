# Importing views.
from django.urls import path
from . import views

# All the url of the app.
urlpatterns = [
	# Get all the users on home page and getting specific user.
	path('', views.allUsers, name='allUsers'),
	path('user/profile/<str:user_id>', views.user_profile, name='user_profile'),

	# Login, Register and logout views.
	path('user/login', views.loginUser, name='user_login'),
	path('user/logout', views.logoutUser, name='user_logout'),
	path('user/register', views.registerUser, name='user_register')
]