from django.urls import path
from . import views

# projects and specific project routes.
urlpatterns = [
	path('projects/', views.all_projects, name='projects'),
	path('project/<str:project_id>', views.specific_project, name='specific_project'),
]