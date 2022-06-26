# Form for user to signup.

# Importing default User model.
from django.contrib.auth.models import User

# Importing forms and default UserCreationForm.
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *

# Form for user to signup.
class SignUpForm(UserCreationForm):
	# Creating a different fields in form.
	username = forms.CharField()
	first_name = forms.CharField()
	last_name=forms.CharField()
	email=forms.EmailField()

	# fields to display.
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	# Do not show help_text of password and change label of password2 to Confirm Password.
	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['password1'].help_text = None
		self.fields['password2'].help_text = None
		self.fields['password2'].label = 'Confirm Password'
	
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'input', 'autocomplete': 'off', 'required': True})

# Form for user to edit their main profile information.
class EditHeadlineForm(forms.ModelForm):
	class Meta:
		model = UserProfileModel
		fields = ('username', 'first_name', 'last_name', 'user_email', 'profession', 'bio', 'location', 'github', 'linkedin', 'twitter', 'youtube', 'website', 'image')

	def __init__(self, *args, **kwargs):
		super(EditHeadlineForm, self).__init__(*args, **kwargs)
		# adding class to all the inputs.
		for field in self.fields.values():
			field.widget.attrs.update({'class': 'input', 'style': 'margin-bottom: 15px'})

# Form for user to add new skill.
class AddSkillForm(forms.ModelForm):
	# Getting a model.
	class Meta:
		model = SkillsModel
		fields = '__all__'

	# Hiding the owner field.
	def __init__(self, user, *args, **kwargs):
		super(AddSkillForm, self).__init__(*args, **kwargs)
		self.fields['owner'].initial = user
		self.fields['owner'].widget = forms.HiddenInput()
		self.fields['owner'].label = ''

		for field in self.fields.values():
			field.widget.attrs.update({'class': 'input', 'placeholder': field.label, 'autocomplete': 'off', 'required': True})

# Form for user to add skill which does not have a description.
class AddOtherSkillForm(forms.ModelForm):
	# Getting a model.
	class Meta:
		model = SkillsModel
		fields = '__all__'

	# Hiding the owner and description field.
	def __init__(self, user, *args, **kwargs):
		super(AddOtherSkillForm, self).__init__(*args, **kwargs)
		self.fields['owner'].initial = user
		self.fields['owner'].widget = forms.HiddenInput()
		self.fields['owner'].label = ''
		self.fields['description'].initial = ''
		self.fields['description'].widget = forms.HiddenInput()
		self.fields['description'].label = ''

		for field in self.fields.values():
			field.widget.attrs.update({'class': 'input', 'placeholder': field.label, 'autocomplete': 'off', 'required': True})

# Form to send a message to a user.
class SendMessages(forms.ModelForm):
	class Meta:
		model = MessagesModel
		fields = ['sender', 'receiver', 'subject', 'message']

	# Hiding the sender, receiver field.
	# Set the initial value of sender to the current user.
	# Set the initial value of receiver to the user who is being messaged.
	def __init__(self, user, receiver, *args, **kwargs):
		super(SendMessages, self).__init__(*args, **kwargs)
		self.fields['sender'].initial = user
		self.fields['sender'].widget = forms.HiddenInput()
		self.fields['sender'].label = ''

		self.fields['receiver'].initial = receiver
		self.fields['receiver'].widget = forms.HiddenInput()
		self.fields['receiver'].label = ''


		for field in self.fields.values():
			field.widget.attrs.update({'class': 'input', 'placeholder': field.label, 'autocomplete': 'off', 'required': True, 'style': 'margin-bottom: 20px'})