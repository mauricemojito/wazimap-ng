# Generated by Django 2.2.10 on 2020-04-02 08:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0057_auto_20200402_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='subindicators',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=list, size=None),
        ),
    ]