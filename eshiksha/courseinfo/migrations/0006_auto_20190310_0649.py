# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0005_auto_20190310_0633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='content',
            name='module',
        ),
        migrations.RemoveField(
            model_name='file',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='image',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='text',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='video',
            name='owner',
        ),
        migrations.AlterModelOptions(
            name='module',
            options={},
        ),
        migrations.RemoveField(
            model_name='module',
            name='order',
        ),
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Text',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
