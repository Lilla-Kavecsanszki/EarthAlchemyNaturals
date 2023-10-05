# Generated by Django 3.2.20 on 2023-10-05 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membership', '0002_remove_membership_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='membership', to=settings.AUTH_USER_MODEL),
        ),
    ]