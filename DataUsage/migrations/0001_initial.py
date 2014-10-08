# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('download', models.DecimalField(max_digits=20, decimal_places=2)),
                ('upload', models.DecimalField(max_digits=20, decimal_places=2)),
                ('total', models.DecimalField(max_digits=20, decimal_places=2)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
