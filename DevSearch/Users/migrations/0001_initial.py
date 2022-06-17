# Generated by Django 4.0.5 on 2022-06-17 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=200)),
                ('user_bio', models.TextField(blank=True, max_length=1000, null=True)),
                ('user_image', models.ImageField(blank=True, default='User/user.png', null=True, upload_to='User/')),
                ('user_github', models.URLField(blank=True, null=True)),
                ('user_linkedin', models.URLField(blank=True, null=True)),
                ('user_twitter', models.URLField(blank=True, null=True)),
                ('user_youtube', models.URLField(blank=True, null=True)),
                ('user_website', models.URLField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]