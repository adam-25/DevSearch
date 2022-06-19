# Generated by Django 4.0.5 on 2022-06-19 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_alter_userprofilemodel_github_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofilemodel',
            name='skills',
        ),
        migrations.AddField(
            model_name='userprofilemodel',
            name='skills',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.skillsmodel'),
        ),
    ]
