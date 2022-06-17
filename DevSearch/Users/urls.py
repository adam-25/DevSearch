from django.urls import path
from . import views

urlpatterns = [
	path('', views.allUsers, name='allUsers'),
	path('user/profile/<str:user_id>', views.user_profile, name='user_profile')
]