# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20151017_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='height',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='width',
        ),
    ]
