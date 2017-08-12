# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_shorturl_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='url_curta',
            field=models.URLField(db_index=True, default=1, verbose_name='URL_CURTA'),
            preserve_default=False,
        ),
    ]