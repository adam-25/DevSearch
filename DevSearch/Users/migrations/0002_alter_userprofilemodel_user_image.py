# Generated by Django 4.0.5 on 2022-06-17 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='user_image',
            field=models.ImageField(blank=True, default='Images/User/user.png', null=True, upload_to='User/'),
        ),
    ]