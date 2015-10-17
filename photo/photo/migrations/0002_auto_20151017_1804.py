# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(to='photo.PhotoUser', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='viewers',
            field=models.ManyToManyField(to='photo.PhotoUser', related_name='can_view'),
        ),
    ]
