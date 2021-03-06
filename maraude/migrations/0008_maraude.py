# Generated by Django 3.0.6 on 2020-06-06 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_auto_20200530_1147'),
        ('maraude', '0007_delete_maraude'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maraude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date de maraude')),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('association', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Association')),
                ('benevole', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Benevole')),
            ],
        ),
    ]
