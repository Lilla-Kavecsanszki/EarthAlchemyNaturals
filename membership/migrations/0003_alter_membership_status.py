# Generated by Django 3.2.20 on 2023-09-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_auto_20230929_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='status',
            field=models.CharField(default='Non-Member', max_length=100),
        ),
    ]
