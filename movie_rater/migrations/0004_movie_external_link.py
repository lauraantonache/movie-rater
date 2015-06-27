# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie_rater', '0003_auto_20150625_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='external_link',
            field=models.CharField(max_length=500, default=datetime.datetime(2015, 6, 27, 8, 43, 22, 298781, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
