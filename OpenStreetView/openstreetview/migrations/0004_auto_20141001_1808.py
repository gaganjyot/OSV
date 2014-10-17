# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openstreetview', '0003_auto_20141001_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_data',
            name='image_path',
            field=models.CharField(max_length=200),
        ),
    ]
