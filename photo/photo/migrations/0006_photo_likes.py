# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_auto_20151017_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
