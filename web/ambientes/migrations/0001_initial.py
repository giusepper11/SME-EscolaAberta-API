# Generated by Django 2.1.5 on 2019-03-14 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('escolas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmbientesUnidadesEdu',
            fields=[
                ('tpamb', models.IntegerField(primary_key=True, serialize=False)),
                ('numsala', models.CharField(blank=True, max_length=6, null=True)),
                ('descamb', models.CharField(blank=True, max_length=70, null=True)),
                ('capfis', models.IntegerField(blank=True, null=True)),
                ('capreal', models.IntegerField(blank=True, null=True)),
                ('metragem', models.IntegerField(blank=True, null=True)),
                ('localizacao', models.CharField(blank=True, max_length=6, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('dt_status', models.DateTimeField(blank=True, null=True)),
                ('padrao', models.CharField(blank=True, max_length=40, null=True)),
                ('flag_ut', models.CharField(blank=True, max_length=1, null=True)),
                ('dt_atualizacao_tabela', models.DateTimeField(blank=True, null=True)),
                ('dt_inicio', models.DateTimeField(blank=True, null=True)),
                ('dt_fim', models.DateTimeField(blank=True, null=True)),
                ('dre', models.CharField(blank=True, max_length=60, null=True)),
                ('tipoesc', models.CharField(blank=True, max_length=12, null=True)),
                ('nomesc', models.CharField(blank=True, max_length=60, null=True)),
                ('database', models.DateField(blank=True, null=True)),
                ('codesc', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='escolas.Escolas')),
            ],
        ),
    ]
