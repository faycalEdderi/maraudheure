# Generated by Django 3.0.6 on 2020-07-02 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maraude', '0019_auto_20200630_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maraude',
            name='heure_fin',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
