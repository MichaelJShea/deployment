# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-25 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0002_auto_20190221_0049'),
        ('wishes', '0002_wishes_wisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Granted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('likes', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('grantor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='granted_wish', to='login_register.User')),
                ('wisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='made_wish', to='wishes.wishes')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_by', to='login_register.User')),
                ('wish_liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='granted_liked', to='wishes.Granted')),
            ],
        ),
    ]
