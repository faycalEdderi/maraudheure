# Generated by Django 3.0.6 on 2020-06-21 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200616_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='benevole',
            name='activite',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='benevole',
            name='hobbies',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='benevole',
            name='metier',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
