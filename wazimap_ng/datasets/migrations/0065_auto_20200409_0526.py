# Generated by Django 2.2.10 on 2020-04-09 04:18

import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import wazimap_ng.datasets.models.upload


def copy_data_to_new_field(apps, schema_editor):
    """
    copy data of Array field subindicator to json field subindicator
    """
    Indicator = apps.get_model('datasets', 'Indicator')

    for indicator in Indicator.objects.all():
        if indicator.subindicators:
            groups = indicator.groups
            data = []
            if groups and len(groups) > 1:
                for idx, subindicator in enumerate(indicator.subindicators):
                    subdata = {}
                    text_list = ""
                    text_list = []
                
                    subindicators = subindicator.split("/")
                    for sidx, val in enumerate(groups):
                        subdata[val] = subindicators[sidx]
                        text_list.append(f"{val}: {subindicators[sidx]}")
                    data.append({
                        "groups": subdata,
                        "id": idx,
                        "label": " / ".join(text_list),
                    })
            elif groups and len(groups) == 1:
                for idx, subindicator in enumerate(indicator.subindicators):
                    data.append({
                        "groups" : {groups[0]: subindicator},
                        "id": idx,
                        "label": f"{groups[0]}: {subindicator}",
                    })

            indicator.subindicators_new = data
            indicator.save()


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0064_merge_20200409_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='subindicators_new',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list, blank=True),
        ),
        migrations.RunPython(copy_data_to_new_field),
        migrations.RemoveField(
            model_name='indicator',
            name='subindicators',
        ),
        migrations.RenameField(
            model_name='indicator',
            old_name='subindicators_new',
            new_name='subindicators',
        ),
    ]
