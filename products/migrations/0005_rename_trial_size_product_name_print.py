# Generated by Django 3.2.20 on 2023-09-16 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_trial_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='trial_size',
            new_name='name_print',
        ),
    ]