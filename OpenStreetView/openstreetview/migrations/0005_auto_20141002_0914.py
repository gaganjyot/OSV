# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openstreetview', '0004_auto_20141001_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_data',
            name='location_x',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='image_data',
            name='location_y',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
    ]
