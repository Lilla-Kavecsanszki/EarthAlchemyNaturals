# Generated by Django 3.2.20 on 2023-10-05 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='user',
        ),
    ]
