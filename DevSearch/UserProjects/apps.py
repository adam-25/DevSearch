from django.apps import AppConfig

class UserprojectsConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'UserProjects'

	# Notifying app to Use signals.
	def ready(self):
		import UserProjects.signals
