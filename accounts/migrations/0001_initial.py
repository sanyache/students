# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-10 11:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_phone', models.CharField(blank=True, default='', max_length=12, verbose_name='\u041c\u043e\u0431\u0456\u043b\u044c\u043d\u0438\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0444\u0456\u043b\u044c \u043a\u043e\u0440\u0438\u0441\u0442\u0443\u0432\u0430\u0447\u0430',
            },
        ),
    ]
