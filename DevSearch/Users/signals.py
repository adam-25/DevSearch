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


# When add new skill then it also apply to the owner of the skill.
@receiver(post_save, sender=SkillsModel)
def addSkillToUserProfile(sender, instance, **kwargs):
	# Skills Model
	skills = instance

	# Get user profile from skills model.
	user_profile = skills.owner

	# Add new skill to user profile.
	user_profile.skills.add(skills)

	# Save the user profile.
	user_profile.save()


# When delete skill then it also apply to the owner of the skill.
@receiver(post_delete, sender=SkillsModel)
def deleteSkillUserProfile(sender, instance, **kwargs):
	# Skills Model
	skill = instance

	# Get user profile depend on the owner of the skill.
	user_profile = skill.owner

	# Delete skill from user profile.
	user_profile.skills.remove(skill)

	# Save the user profile.
	user_profile.save()