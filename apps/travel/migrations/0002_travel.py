# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-24 05:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('books', models.ManyToManyField(related_name='Travels', to='travel.user')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planner', to='travel.user')),
            ],
        ),
    ]
