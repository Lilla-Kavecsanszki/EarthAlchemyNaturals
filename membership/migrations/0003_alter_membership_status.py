# Generated by Django 3.2.20 on 2023-10-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_alter_membership_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='status',
            field=models.CharField(choices=[('Member', 'Member'), ('None', 'None')], default='None', max_length=100),
        ),
    ]
