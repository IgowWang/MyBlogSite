# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150623_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='class_name',
            field=models.ForeignKey(to='blog.Classification', verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', blank=True, verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='belong_to',
            field=models.ForeignKey(verbose_name='title', to='blog.Articles', blank='', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(verbose_name='user_name', to='blog.User', blank='', null=True),
        ),
    ]
