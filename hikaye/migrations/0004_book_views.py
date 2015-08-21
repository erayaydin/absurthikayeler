# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hikaye', '0003_auto_20150821_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='views',
            field=models.BigIntegerField(default=0),
        ),
    ]
