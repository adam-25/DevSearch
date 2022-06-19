# Form for user to signup.

# Importing default User model.
from django.contrib.auth.models import User

# Importing forms and default UserCreationForm.
from django import forms
from django.contrib.auth.forms import UserCreationForm

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