# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32)),
                ('body', models.TextField()),
                ('slug', models.CharField(unique=True, max_length=128)),
                ('meta_title', models.CharField(help_text=b'http://www.seomoz.org/learn-seo/title-tag', max_length=70, null=True, blank=True)),
                ('meta_description', models.CharField(help_text=b'For tips, see http://www.seomoz.org/learn-seo/meta-description', max_length=155, null=True, blank=True)),
                ('published', models.BooleanField(default=False)),
                ('publication_date', models.DateField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(related_name='posts', to='core.Author')),
                ('categories', models.ManyToManyField(related_name='posts', to='core.BlogCategory')),
            ],
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='core.BlogTag'),
        ),
    ]
