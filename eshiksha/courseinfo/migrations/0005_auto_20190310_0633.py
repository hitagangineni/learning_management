# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import courseinfo.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0004_auto_20190310_0606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=courseinfo.fields.OrderField(default=' ', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=courseinfo.fields.OrderField(default=' ', blank=True),
            preserve_default=False,
        ),
    ]
