# Generated by Django 2.1.5 on 2019-02-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nucleo',
            old_name='nome',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='nucleo',
            name='horario_func',
        ),
        migrations.RemoveField(
            model_name='nucleo',
            name='idade_minima',
        ),
        migrations.AddField(
            model_name='nucleo',
            name='month',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='nucleo',
            name='year',
            field=models.IntegerField(default=2019),
        ),
    ]
