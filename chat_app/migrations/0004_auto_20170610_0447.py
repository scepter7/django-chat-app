# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 02:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0003_auto_20170610_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]