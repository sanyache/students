# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-29 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name="\u0406\u043c'\u044f")),
                ('last_name', models.CharField(max_length=256, verbose_name='\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435')),
                ('middle_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='\u041f\u043e-\u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456')),
                ('birthday', models.DateField(null=True, verbose_name='\u0414\u0435\u043d\u044c \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f')),
                ('photo', models.ImageField(null=True, upload_to=b'', verbose_name='\u0424\u043e\u0442\u043e')),
                ('ticket', models.CharField(max_length=30, verbose_name='\u0411\u0456\u043b\u0435\u0442')),
                ('notes', models.TextField(blank=True, verbose_name='\u041d\u043e\u0442\u0430\u0442\u043a\u0438')),
            ],
            options={
                'ordering': ['last_name'],
                'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442',
                'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438',
            },
        ),
    ]
