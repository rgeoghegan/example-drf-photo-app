# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20151017_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='viewers',
            field=models.ManyToManyField(related_name='can_view', to='photo.PhotoUser', blank=True),
        ),
    ]
