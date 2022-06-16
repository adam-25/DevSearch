from django.forms import ModelForm
from .models import *

# Form which can be used as a model form to create a new project.
class ProjectForm(ModelForm):
	class Meta:
		model = ProjectsModel
		fields = ['project_title', 'project_description', 'project_demo', 'source_code', 'project_skills', 'project_image']