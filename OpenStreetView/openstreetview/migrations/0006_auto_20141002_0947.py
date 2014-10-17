# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openstreetview', '0005_auto_20141002_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_data',
            name='location_x',
            field=models.DecimalField(max_digits=6, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='image_data',
            name='location_y',
            field=models.DecimalField(max_digits=6, decimal_places=5),
        ),
    ]
