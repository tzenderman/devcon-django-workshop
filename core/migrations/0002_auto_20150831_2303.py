# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'verbose_name_plural': 'Blog categories'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
