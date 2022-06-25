import re
from django.db.models.signals import *
from django.dispatch import receiver

from .models import *

@receiver(post_save, sender=ProjectReviewModel)
def update_project_reviews(sender, created, instance, **kwargs):
	if created:
		review = instance

		# Update the reviews of the project.
		project = review.project
		# Add review to the project.
		project.project_reviews.add(review)

		# Update the average review of the project.
		project.total_votes += 1
		
		total_up_votes = project.project_reviews.filter(value='up').count()

		if project.total_votes > 0:
			project.vote_ratio = (total_up_votes / project.total_votes) * 100
		else:
			project.vote_ratio = 0

		# Update Project reviews.
		project.save()

@receiver(post_delete, sender=ProjectReviewModel)
def delete_project_reviews(sender, instance, **kwargs):
	review = instance

	# Update the reviews of the project.
	project = review.project
	# Add review to the project.
	project.project_reviews.remove(review)

	# Update the average review of the project.
	project.total_votes -= 1

	total_up_votes = project.project_reviews.filter(value='up').count()

	if project.total_votes > 0:
		project.vote_ratio = (total_up_votes / project.total_votes) * 100
	else:
		project.vote_ratio = 0

	# Update Project reviews.
	project.save()