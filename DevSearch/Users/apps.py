from django.apps import AppConfig


class UsersConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'Users'

	# Notifying app to Use signals.
	def ready(self):
		import Users.signals
