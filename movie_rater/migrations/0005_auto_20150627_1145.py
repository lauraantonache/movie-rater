# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_rater', '0004_movie_external_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='external_link',
        ),
        migrations.AddField(
            model_name='movie',
            name='extern_link',
            field=models.CharField(max_length=500, default='http://www.imdb.com'),
            preserve_default=False,
        ),
    ]
