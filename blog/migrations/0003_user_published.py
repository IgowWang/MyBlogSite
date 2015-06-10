# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150609_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
