# Importing models and User default model.
from re import L
from django.db import models
from django.contrib.auth.models import User

# Create model id.
from uuid import uuid4

from django.forms import ValidationError

# Create your models here.
# Model to contain the profile of an user.
class UserProfileModel(models.Model):
	# One to One relationship with User model.
	# One user can have only one profile. One profile can have only one user.
	# profile get deleted when user is deleted.
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	username = models.CharField(max_length=100, unique=True)
	user_email = models.EmailField(max_length=200, unique=True)
	profession = models.CharField(max_length=200)
	location = models.CharField(max_length=300, blank=True, null=True)

	# Many to many relationship with SkillsModel.
	skills = models.ManyToManyField('SkillsModel')
	bio = models.TextField(max_length=10000)
	image = models.ImageField(upload_to="Images/User/UserImages", default="Images/User/user.png", blank=True)
	github = models.CharField(max_length=500, blank=True, null=True)
	linkedin = models.CharField(max_length=500, blank=True, null=True)
	twitter = models.CharField(max_length=500, blank=True, null=True)
	youtube = models.CharField(max_length=5000, blank=True, null=True)
	website = models.CharField(max_length=500, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

	# Display profile obj name as first_name and last_name.
	def __str__(self):
		return str(self.first_name + " " + self.last_name)

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

# SkillsModel to contain the skills of an user.
class SkillsModel(models.Model):
	# Name, and description of skills.
	# Owner of the skill.
	owner = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid4)

	# Display the name of skill as an object of this model.
	def __str__(self):
		return str(self.name)

# Message model.
class MessagesModel(models.Model):
	# Sender and receiver of the message.
	sender = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE, null=True)
	receiver = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE, related_name='receiver')
	subject = models.CharField(max_length=500)
	message = models.TextField()
	read_message = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid4)

	def __str__(self):
		return str(self.subject)

	# If sender and receiver are same, raise ValidationError.
	def clean(self):
		if self.receiver == self.sender:
			raise ValidationError("Users can't send message to themselves.")

	def save(self, *args, **kwargs):
		self.full_clean()
		super().save(*args, **kwargs)