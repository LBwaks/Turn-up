# Generated by Django 3.2.4 on 2021-09-11 14:24

import autoslug.fields
import ckeditor.fields
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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venue_category_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='venue_name', unique=True)),
                ('event_name', models.CharField(max_length=255)),
                ('event_start_date', models.DateTimeField()),
                ('event_stop_date', models.DateTimeField()),
                ('event_description', ckeditor.fields.RichTextField()),
                ('event_offer', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('speaker_artist', models.CharField(blank=True, max_length=255, null=True)),
                ('event_fee', models.CharField(blank=True, max_length=255, null=True)),
                ('event_group_charge', models.IntegerField(blank=True, null=True)),
                ('event_group_charge_number', models.IntegerField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, default='venue_event_photo/venues.jpg', null=True, upload_to='venue_event_photo/')),
                ('is_featured', models.BooleanField(default=False)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('venue_county', models.CharField(choices=[('Mombasa', 'Mombasa'), ('Kwale', 'Kwale'), ('Kilifi', 'Kilifi'), ('Tana River', 'Tana River'), ('Lamu', 'Lamu'), ('Taita-Taveta', 'Taita-Taveta'), ('Garissa', 'Garissa'), ('Wajir', 'Wajir'), ('Mandera', 'Mandera'), ('Marsabit', 'Marsabit'), ('Isiolo', 'Isiolo'), ('MERU', 'Meru'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Embu', 'Embu'), ('Kitui', 'Kitui'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Kirinyaga', 'Kirinyaga'), ('Muranga', "Murang'a"), ('Kiambu', 'Kiambu'), ('Turkana', 'Turkana'), ('West Pokot', ' West Pokot'), ('Samburu', 'Samburu'), ('Trans Nzoia', 'Trans Nzoia'), ('Uasin Gishu', 'Uasin Gishu'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Nandi', 'Nandi'), ('Baringo', 'Baringo'), ('Laikipia', 'Laikipia'), ('Nakuru', 'Nakuru'), ('Narok', 'Narok'), ('Kajiado', 'Kajiado'), ('Kericho', 'Kericho'), ('Bomet', 'Bomet'), ('Kakamega', 'Kakamega'), ('Vihiga', 'Vihiga'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Siaya', 'Siaya'), ('Kisumu', 'Kisumu'), ('Homa Bay', 'Homa Bay'), ('Migori', 'Migori'), ('Kisii', 'Kisii'), ('Nyamira', 'Nyamira'), ('Nairobi', 'Nairobi')], default='Nairobi', max_length=20)),
                ('venue_location', models.CharField(max_length=100)),
                ('venue_view', models.IntegerField(db_index=True, default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='venue_category', to='venues.category')),
                ('likes', models.ManyToManyField(blank=True, related_name='Venue_likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commenting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenting', to='venues.venue')),
            ],
        ),
    ]
