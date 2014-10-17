# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image_data',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('image_path', models.CharField(max_length=20)),
                ('location_x', models.FloatField()),
                ('location_y', models.FloatField()),
                ('approvals', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
