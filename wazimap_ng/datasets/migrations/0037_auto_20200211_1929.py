# Generated by Django 2.2.8 on 2020-02-11 19:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0036_auto_20200209_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='groups',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None),
        ),
    ]
