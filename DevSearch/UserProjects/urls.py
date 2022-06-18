from django.urls import path
from . import views

# projects and specific project routes.
urlpatterns = [
	# All projects.
	path('projects/', views.all_projects, name='projects'),
	# Specific project.
	path('project/<str:project_id>', views.specific_project, name='specific_project'),
	# Create a new project.
	path('projects/create', views.create_project, name='create_project'),

	# Delete or update a specific project.
	path('projects/update/<str:project_id>', views.update_project, name='update_project'),
	path('projects/delete/<str:project_id>', views.delete_project_confirmation, name='delete_project'),
]