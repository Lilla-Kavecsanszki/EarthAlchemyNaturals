# Generated by Django 3.2.20 on 2023-10-12 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('default_street_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('default_street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('default_town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('default_county', models.CharField(blank=True, max_length=80, null=True)),
                ('default_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('membership_start_date', models.DateTimeField(blank=True, null=True)),
                ('membership_duration', models.DurationField(blank=True, null=True)),
                ('membership_status', models.ForeignKey(default=profiles.models.get_non_member_status, on_delete=django.db.models.deletion.PROTECT, related_name='user_membership', to='membership.membership')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VIPBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_packaging_color', models.CharField(choices=[('pink', 'Pink Box'), ('gold', 'Gold Box')], default='pink', max_length=10)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
            options={
                'verbose_name_plural': 'VIP boxes',
            },
        ),
    ]
