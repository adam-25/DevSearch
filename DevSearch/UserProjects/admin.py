from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ProjectsModel)
admin.site.register(ProjectSkillTagsModel)
admin.site.register(ProjectReviewModel)