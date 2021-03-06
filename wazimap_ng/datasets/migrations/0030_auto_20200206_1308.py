# Generated by Django 2.2.8 on 2020-02-06 13:08

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0029_indicatordata'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='universe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasets.Universe'),
        ),
        migrations.AlterField(
            model_name='indicatordata',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
    ]
