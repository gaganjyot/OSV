# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openstreetview', '0006_auto_20141002_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_data',
            name='location_x',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='image_data',
            name='location_y',
            field=models.FloatField(),
        ),
    ]
