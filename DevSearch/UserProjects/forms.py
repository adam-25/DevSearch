# Importing django Model forms
from django.forms import ModelForm
from django import forms

# Importing models of Project.
from .models import *

# Form which can be used as a model form to create a new project.
class ProjectForm(ModelForm):
	class Meta:
		# form based on model.
		model = ProjectsModel

		# Fields to render in html template.
		fields = ['project_title', 'project_description', 'project_demo', 'source_code', 'project_skills', 'project_image']
		# making project_skills input as a checkbox.
		widgets = {
			'project_skills': forms.CheckboxSelectMultiple(),
		}

	# applying to class to inputs of the form.
	# Place holder to each input.
	def __init__(self, user, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		self.fields['project_skills'].widget = forms.CheckboxSelectMultiple()
		self.fields['project_skills'].queryset = SkillsModel.objects.filter(owner=user)
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'input', 'placeholder': field.label, 'autocomplete': 'off'})