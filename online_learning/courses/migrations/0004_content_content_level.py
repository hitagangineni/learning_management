# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20190310_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='content_level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
