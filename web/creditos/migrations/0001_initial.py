# Generated by Django 2.1.5 on 2019-02-11 14:12

import creditos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('value', models.FloatField(default=0, validators=[creditos.models.validate_floatPositivos])),
            ],
        ),
    ]
