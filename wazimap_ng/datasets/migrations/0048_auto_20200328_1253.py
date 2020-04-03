# Generated by Django 2.2.10 on 2020-03-28 12:53

import django.core.validators
from django.db import migrations, models
import wazimap_ng.datasets.models.upload


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0047_auto_20200325_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetfile',
            name='document',
            field=models.FileField(help_text='\n            Uploaded document should be less than 3000.0 MiB in size and \n            file extensions should be one of xls, xlsx, csv.\n        ', upload_to=wazimap_ng.datasets.models.upload.get_file_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xls', 'xlsx', 'csv']), wazimap_ng.datasets.models.upload.file_size]),
        ),
    ]