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
		fields = ['project_owner', 'project_title', 'project_description', 'project_demo', 'source_code', 'project_skills', 'project_image']
	
	# applying to class to inputs of the form.
	# Place holder to each input.
	def __init__(self, user, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		# Project skills checkbox.add()
		self.fields['project_skills'].widget = forms.CheckboxSelectMultiple()

		# Get only projects skill which belongs to the user.
		self.fields['project_skills'].queryset = SkillsModel.objects.filter(owner=user)

		# Project owner assigning and hiding the field and label.
		self.fields['project_owner'].initial = user
		self.fields['project_owner'].widget = forms.HiddenInput()
		self.fields['project_owner'].label = ''

		for field in self.fields.values():
			field.widget.attrs.update({'class': 'input', 'placeholder': field.label, 'autocomplete': 'off'})