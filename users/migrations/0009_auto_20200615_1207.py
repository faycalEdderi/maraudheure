# Generated by Django 3.0.6 on 2020-06-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200615_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='date_creation',
            field=models.DateField(),
        ),
    ]
