# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', django_markdown.models.MarkdownField()),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('calss_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('comment', django_markdown.models.MarkdownField()),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('user_name', models.CharField(unique=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='class_name',
            field=models.ForeignKey(to='blog.Classification'),
        ),
        migrations.AddField(
            model_name='articles',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', blank=True),
        ),
    ]
