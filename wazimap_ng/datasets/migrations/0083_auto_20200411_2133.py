# Generated by Django 2.2.10 on 2020-04-11 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0082_delete_indicatorsubcategory'),
    ]

    database_operations = [
        migrations.AlterModelTable('Profile', 'profile_profile'),  
    ]

    state_operations = [

    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]