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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', django_markdown.models.MarkdownField()),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('calss_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('comment', django_markdown.models.MarkdownField()),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('belong_to', models.ForeignKey(null=True, verbose_name='title', to='blog.Articles')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tag_name', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, verbose_name='user_name', to='blog.User'),
        ),
        migrations.AddField(
            model_name='articles',
            name='class_name',
            field=models.ForeignKey(verbose_name='class_name', to='blog.Classification'),
        ),
        migrations.AddField(
            model_name='articles',
            name='tags',
            field=models.ManyToManyField(verbose_name='tag_name', blank=True, to='blog.Tag'),
        ),
    ]
