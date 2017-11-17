# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-29 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('leader', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Student', verbose_name='\u0421\u0430\u0442\u0440\u043e\u0441\u0442\u0430')),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u0430',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u0438',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Group', verbose_name='\u0413\u0440\u0443\u043f\u0430'),
        ),
    ]