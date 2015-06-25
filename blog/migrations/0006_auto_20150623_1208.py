# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150619_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classification',
            old_name='calss_name',
            new_name='class_name',
        ),
    ]
