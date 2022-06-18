from gettext import install
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import *
from .models import *

# Save UserProfile when User is created.
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
	if created:
		user = instance
		profile = UserProfileModel.objects.create(
			user = user,
			first_name = user.first_name,
			last_name = user.last_name,
			username = user.username,
			user_email = user.email,
		)
		profile.save()
	else:
		user = instance
		profile = UserProfileModel.objects.filter(user=user).update(
			first_name = user.first_name,
			last_name = user.last_name,
			username = user.username,
			user_email = user.email,
		)


@receiver(post_delete, sender=UserProfileModel)
def deleteUser(sender, instance, **kwargs):
	user = instance.user
	user.delete()

