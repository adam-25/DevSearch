# Generated by Django 4.0.5 on 2022-06-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_skillsmodel_rename_user_bio_userprofilemodel_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='location',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]