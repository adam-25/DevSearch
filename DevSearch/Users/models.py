from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class UserProfileModel(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	user_email = models.EmailField(max_length=200)
	profession = models.CharField(max_length=200)
	skills = models.ManyToManyField('SkillsModel')
	bio = models.TextField(max_length=10000, blank=True, null=True)
	image = models.ImageField(upload_to="User/", default="Images/User/user.png", blank=True, null=True)
	github = models.URLField(max_length=500, blank=True, null=True)
	linkedin = models.URLField(max_length=500, blank=True, null=True)
	twitter = models.URLField(max_length=500, blank=True, null=True)
	youtube = models.URLField(max_length=5000, blank=True, null=True)
	website = models.URLField(max_length=500, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

	def __str__(self):
		return str(self.first_name + " " + self.last_name)

class SkillsModel(models.Model):
	name = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid4)

	def __str__(self):
		return str(self.name)