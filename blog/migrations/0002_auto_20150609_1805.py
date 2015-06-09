# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('ID', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('comment', django_markdown.models.MarkdownField()),
                ('created_at', models.DateTimeField(verbose_name='created date')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', django_markdown.models.MarkdownField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('publish', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Blog Entries',
                'verbose_name': 'Blog Entry',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('ID', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('admin', models.BooleanField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(verbose_name='created date')),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
