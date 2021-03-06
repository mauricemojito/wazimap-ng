# Generated by Django 2.2.10 on 2020-05-21 15:01

from django.db import migrations

def set_profile_to_private(apps, schema_editor):
    Profile = apps.get_model("profile", "Profile")
    for profile in Profile.objects.filter(requires_authentication=True):
    	profile.permission_type = "private"
    	profile.save()


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0036_auto_20200508_0751'),
    ]

    operations = [
    	migrations.RunPython(set_profile_to_private),
    ]
