# signals.py: This file throws some specific events after, before particular events.

# Importing User and app models.
from django.contrib.auth.models import User
from .models import *

# Importing signals.
from django.dispatch import receiver
from django.db.models.signals import *


# Save UserProfile when User is created.
# When User model save first time then we create a profile model.
# If User model updates then profile updates as well.
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
	# If profile is created first time.
	if created:
		# Get user.
		user = instance
		# Create a profile with specific values.
		profile = UserProfileModel.objects.create(
			user = user,
			first_name = user.first_name,
			last_name = user.last_name,
			username = user.username,
			user_email = user.email,
		)
		# Save the profile.
		profile.save()
	else:
		# Get user.
		user = instance
		# Update the profile with specific values.
		profile = UserProfileModel.objects.filter(user=user).update(
			first_name = user.first_name,
			last_name = user.last_name,
			username = user.username,
			user_email = user.email,
		)


# When Profile model is deleted then user is deleted.
@receiver(post_delete, sender=UserProfileModel)
def deleteUser(sender, instance, **kwargs):
	# Get user from profile model.
	# Delete user.
	user = instance.user
	user.delete()
