# Generated by Django 3.0.6 on 2020-06-06 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200530_1147'),
        ('maraude', '0004_maraude'),
    ]

    operations = [
        migrations.AddField(
            model_name='maraude',
            name='benevole',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Benevole'),
        ),
    ]