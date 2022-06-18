from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

	# Add Users and UserProjects app urls.
	path('', include('UserProjects.urls')),
	path('', include('Users.urls')),
]

# Appending MEDIA_URL to urlpatterns so, user upload can be stored in specific folder mentioned in MEDIA_URL.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)