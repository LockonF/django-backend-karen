# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-06 19:56
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
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('direccion', models.CharField(blank=True, default='', max_length=500)),
                ('telefono', models.CharField(max_length=15)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='persona', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Persona',
            },
        ),
    ]