# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-01 16:18
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import mysite.storage_backends


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('upload', models.FileField(storage=mysite.storage_backends.PrivateMediaStorage(), upload_to='')),
                ('transcoded', models.FileField(storage=mysite.storage_backends.PrivateMediaStorage(), blank=True,
                                                default=None, null=True, upload_to='')),
                ('thumbnail', models.FileField(storage=mysite.storage_backends.PrivateMediaStorage(), blank=True,
                                               default=None, null=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents',
                                           to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=16)),
                ('inputObject', models.CharField(max_length=1024)),
                ('outputObject', models.CharField(max_length=1024)),
                ('thumbnail', models.CharField(max_length=1024)),
            ],
        ),
    ]
