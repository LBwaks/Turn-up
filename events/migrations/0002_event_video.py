# Generated by Django 3.2.4 on 2021-09-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='event_events_videos/'),
        ),
    ]
