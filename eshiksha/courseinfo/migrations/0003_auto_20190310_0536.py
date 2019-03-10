# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0002_chapter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('levelofmodule', models.IntegerField(blank=True)),
                ('course', models.ForeignKey(related_name='modules', to='courseinfo.Course')),
            ],
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='course',
        ),
        migrations.DeleteModel(
            name='Chapter',
        ),
    ]
