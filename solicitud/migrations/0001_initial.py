# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 04:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=40, null=True)),
                ('texto', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_creacion', models.DateField(blank=True, default=datetime.datetime.now)),
                ('respuesta', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.CharField(blank=True, default=b'Pendiente', max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSolicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='solicitud',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Tipo', to='solicitud.TipoSolicitud'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='usuario_creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asistente', to='usuario.Usuario'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='usuario_destino',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cientifico', to='usuario.Usuario'),
        ),
    ]
