from re import template
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

	# Add Users and UserProjects app urls.
	path('', include('UserProjects.urls')),
	path('', include('Users.urls')),

	# URLs to sent reset Password.

	# Page to take an email to send a link to reset password,
	path('user/forgot_password', auth_views.PasswordResetView.as_view(template_name='Users/ResetPassword/resetPasswordEmail.html'), name='reset_password'),

	# Page shows that link has been sent successfully.
	path('user/reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='Users/ResetPassword/resetLinkConfirmation.html'), name='password_reset_done'),

	# Page to reset password.
	path('user/reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='Users/ResetPassword/enterNewPassword.html'), name='password_reset_confirm'),

	# Confirmation that password has been reset successfully.
	path('user/password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='Users/ResetPassword/resetPasswordSuccess.html'), name='password_reset_complete'),
]

# Appending MEDIA_URL to urlpatterns so, user upload can be stored in specific folder mentioned in MEDIA_URL.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)