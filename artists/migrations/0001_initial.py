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
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='artist_name', unique=True)),
                ('event_name', models.CharField(max_length=100)),
                ('event_description', ckeditor.fields.RichTextField()),
                ('event_offer', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('event_charge', models.IntegerField(blank=True, default='Free Entry', null=True)),
                ('event_group_charge', models.IntegerField(blank=True, null=True)),
                ('event_group_charge_number', models.IntegerField(blank=True, null=True)),
                ('event_start_date', models.DateTimeField()),
                ('event_end_date', models.DateTimeField()),
                ('photo', models.ImageField(default='artists_events_photos/artists.jpg', upload_to='artists_events_photos/')),
                ('is_featured', models.BooleanField(default=False)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('event_county', models.CharField(choices=[('Mombasa', 'Mombasa'), ('Kwale', 'Kwale'), ('Kilifi', 'Kilifi'), ('Tana River', 'Tana River'), ('Lamu', 'Lamu'), ('Taita-Taveta', 'Taita-Taveta'), ('Garissa', 'Garissa'), ('Wajir', 'Wajir'), ('Mandera', 'Mandera'), ('Marsabit', 'Marsabit'), ('Isiolo', 'Isiolo'), ('MERU', 'Meru'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Embu', 'Embu'), ('Kitui', 'Kitui'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Kirinyaga', 'Kirinyaga'), ('Muranga', "Murang'a"), ('Kiambu', 'Kiambu'), ('Turkana', 'Turkana'), ('West Pokot', ' West Pokot'), ('Samburu', 'Samburu'), ('Trans Nzoia', 'Trans Nzoia'), ('Uasin Gishu', 'Uasin Gishu'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Nandi', 'Nandi'), ('Baringo', 'Baringo'), ('Laikipia', 'Laikipia'), ('Nakuru', 'Nakuru'), ('Narok', 'Narok'), ('Kajiado', 'Kajiado'), ('Kericho', 'Kericho'), ('Bomet', 'Bomet'), ('Kakamega', 'Kakamega'), ('Vihiga', 'Vihiga'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Siaya', 'Siaya'), ('Kisumu', 'Kisumu'), ('Homa Bay', 'Homa Bay'), ('Migori', 'Migori'), ('Kisii', 'Kisii'), ('Nyamira', 'Nyamira'), ('Nairobi', 'Nairobi')], default='Nairobi', max_length=20)),
                ('event_location', models.CharField(max_length=100)),
                ('artist_view', models.IntegerField(db_index=True, default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='artists.artist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='artist',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='Artist_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
