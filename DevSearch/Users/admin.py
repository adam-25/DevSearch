from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfileModel)
admin.site.register(SkillsModel)
admin.site.register(MessagesModel)