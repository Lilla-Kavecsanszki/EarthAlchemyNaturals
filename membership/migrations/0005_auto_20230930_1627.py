# Generated by Django 3.2.20 on 2023-09-30 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_alter_membership_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='VIPBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_packaging_color', models.CharField(choices=[('pink', 'Pink Box'), ('gold', 'Gold Box')], default='pink', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='choose_vip_box',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='membership',
            name='vip_box',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='membership', to='membership.vipbox'),
        ),
    ]