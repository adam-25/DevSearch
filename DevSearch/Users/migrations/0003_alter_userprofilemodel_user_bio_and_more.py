# Generated by Django 4.0.5 on 2022-06-17 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_userprofilemodel_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='user_bio',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='user_github',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='user_linkedin',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='user_twitter',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='user_website',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='user_youtube',
            field=models.URLField(blank=True, max_length=5000, null=True),
        ),
    ]
