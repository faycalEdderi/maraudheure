# Generated by Django 3.0.6 on 2020-06-10 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200530_1147'),
        ('maraude', '0011_auto_20200610_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maraude',
            name='association',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_maraude', to='users.Association'),
        ),
    ]