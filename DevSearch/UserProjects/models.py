# Importing models and uuid to get 16 or 32 bit long id.
from django.db import models
import uuid

# Importing models from Users app.
from Users.models import *
# Create your models here.

# Project Model.
class ProjectsModel(models.Model):
	# One to Many Relationship with the project.
	# One Profile can have multiple Projects but one project can only have one user.
	# Project gets deleted when profile gets delete.
	project_owner = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE, null=True)
	project_title = models.CharField(max_length=200)
	project_description = models.TextField()
	project_demo = models.CharField(max_length=1000, null=True, blank=True)
	source_code = models.CharField(max_length=1000, null=True, blank=True)
	# ManyToMany Relationship with the skills model.
	project_skills = models.ManyToManyField(SkillsModel)
	project_image = models.ImageField(upload_to='Images/Project/ProjectImagesUser/', blank=True, default='Images/Project/default.jpg')
	project_reviews = models.ManyToManyField('ProjectReviewModel', blank=True)
	total_votes = models.IntegerField(default=0, null=True, blank=True)
	vote_ratio = models.IntegerField(default=0, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)

	# Show name of the project as the object name.
	def __str__(self):
		return self.project_title
	
	# Get the image url of the project.
	# property to use imageURL method as static.
	@property
	def imageURL(self):
		try:
			url = self.project_image.url
		except:
			url = ''
		return url

# Review Model to store the reviews of the project.
class ProjectReviewModel(models.Model):
	# Can only vote wither up or down.
	# Shown name will be either "Up Vote" or "Down Vote"
	VOTE = [
		('up', 'Up Vote'),
		('down', 'Down Vote'),
	]
	# One to Many relationship with project and user profile.
	# One user can only vote once for one project.
	# One project can have multiple reviews.
	# One user can have multiple reviews for multiple projects.
	# Review gets deleted when project or user profile gets deleted.
	reviewer = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
	project = models.ForeignKey(ProjectsModel, on_delete=models.CASCADE)
	review_body = models.TextField(null=True, blank=True)
	# value have choice of up or down.
	value = models.CharField(max_length=100, choices=VOTE)
	created_at = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)

	class Meta:
		unique_together = ('reviewer', 'project')

	# Show name of the review as the object name.
	def __str__(self):
		return self.value