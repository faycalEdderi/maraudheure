# Generated by Django 3.0.6 on 2020-06-29 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maraude', '0017_auto_20200615_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maraude',
            name='heure_debut',
            field=models.DateField(blank=True, null=True),
        ),
    ]