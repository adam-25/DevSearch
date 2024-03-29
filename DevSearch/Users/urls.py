# Importing views.
from django.urls import path
from . import views

# All the url of the app.
urlpatterns = [
	# Get all the users on home page and getting specific user.
	path('', views.allUsers, name='allUsers'),
	path('user/profile/<str:user_id>', views.userProfile, name='user_profile'),

	# Login, Register and logout views.
	path('user/login', views.loginUser, name='user_login'),
	path('user/logout', views.logoutUser, name='user_logout'),
	path('user/register', views.registerUser, name='user_register'),

	# User can view, edit their account.
	path('user/account', views.user_account, name='user_account'),
	path('user/edit/profile', views.edit_account_profile, name='edit_account'),

	# User to add new skill.
	path('user/add/top_skills', views.add_top_skill, name='add_top_skill'),
	path('user/add/other_skills', views.add_other_skill, name='add_other_skill'),
	# User to edit their skill.
	path('user/edit/top_skills/<str:skill_id>', views.edit_top_skill, name='edit_top_skill'),
	path('user/edit/other_skill/<str:skill_id>', views.edit_other_skill, name='edit_other_skill'),
	# User to delete their skill.
	path('user/delete/skill/<str:skill_id>', views.delete_skill, name='delete_skill'),

	# User check inbox and particular message depending upon id.
	path('user/inbox', views.inbox, name='inbox'),
	path('user/inbox/message/<str:message_id>', views.specific_message, name='specific_message'),

	# User send message to another user depending upon another user id.
	path('user/send_message/<str:user_id>', views.send_message, name='send_message'),

	path('user/deleteAccount/', views.deleteAccount, name='deleteAccount'),
]