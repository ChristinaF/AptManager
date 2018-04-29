# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-28 21:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curr_res', '0002_tenant_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='apt_address',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='apt_city',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='username',
        ),
        migrations.AddField(
            model_name='tenant',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apartment',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curr_res.Tenant'),
        ),
    ]
