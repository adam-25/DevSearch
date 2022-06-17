from django.forms import ModelForm
from django import forms
from .models import *

# Form which can be used as a model form to create a new project.
class ProjectForm(ModelForm):
	class Meta:
		model = ProjectsModel
		fields = ['project_title', 'project_description', 'project_demo', 'source_code', 'project_skills', 'project_image']
		widgets = {
			'project_skills': forms.CheckboxSelectMultiple(),
		}

	def __init__(self, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'input', 'placeholder': field.label + '...', 'autocomplete': 'off'})