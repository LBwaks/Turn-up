# Generated by Django 3.2.4 on 2021-09-26 14:41

import django.contrib.postgres.indexes
from django.db import migrations
from django.contrib.postgres.operations import BtreeGinExtension


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0006_auto_20210918_0935'),
    ]

    operations = [
        BtreeGinExtension(),
        migrations.AddIndex(
            model_name='artist',
            index=django.contrib.postgres.indexes.GinIndex(fields=['artist_name', 'event_name'], name='NewGinIndex'),
        ),
    ]