# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 11:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('microbot', '0005_auto_20160315_0714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, editable=False, max_length=30, unique=True)),
                ('enabled', models.BooleanField(default=True, verbose_name='Enable')),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hooks', to='microbot.Bot', verbose_name='Bot')),
            ],
            options={
                'verbose_name': 'Hook',
                'verbose_name_plural': 'Hooks',
            },
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('hook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipients', to='microbot.Hook', verbose_name='Recipient')),
            ],
            options={
                'verbose_name': 'Recipient',
                'verbose_name_plural': 'Recipients',
            },
        ),
        migrations.AlterModelOptions(
            name='response',
            options={'verbose_name': 'Response', 'verbose_name_plural': 'Responses'},
        ),
        migrations.AddField(
            model_name='hook',
            name='response',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='microbot.Response', verbose_name='Response'),
        ),
    ]