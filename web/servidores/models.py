from django.db import models


# Create your models here.
class Servidores(models.Model):
    cd_serv_sme = models.TextField(blank=True, null=True)
    mes_nasc = models.FloatField(blank=True, null=True)
    ano_nasc = models.FloatField(blank=True, null=True)
    idade = models.FloatField(blank=True, null=True)
    cd_sexo = models.TextField(blank=True, null=True)
    cd_municipio_nasc = models.IntegerField(blank=True, null=True)
    dc_municipio_nasc = models.CharField(max_length=100, blank=True, null=True)
    uf_municipio_nasc = models.CharField(max_length=2, blank=True, null=True)
    cd_pais_nasc = models.IntegerField(blank=True, null=True)
    dc_pais_nasc = models.CharField(max_length=50, blank=True, null=True)
    cd_municipio_res = models.IntegerField(blank=True, null=True)
    dc_municipio_res = models.CharField(max_length=100, blank=True, null=True)
    uf_municipio_res = models.CharField(max_length=2, blank=True, null=True)
    cd_raca_cor = models.IntegerField(blank=True, null=True)
    dc_raca_cor = models.CharField(max_length=20, blank=True, null=True)
    cd_def = models.IntegerField(blank=True, null=True)
    dc_def = models.CharField(max_length=70, blank=True, null=True)
    nivel_form = models.TextField(blank=True, null=True)
    dc_sit_func = models.CharField(max_length=40, blank=True, null=True)
    cd_cargo_base = models.IntegerField(blank=True, null=True)
    dc_cargo_base = models.CharField(max_length=70, blank=True, null=True)
    cd_area_atuacao_base = models.IntegerField(blank=True, null=True)
    dc_area_atuacao_base = models.CharField(max_length=70, blank=True, null=True)
    dt_inicio_cargo_base = models.TextField(blank=True, null=True)
    cd_unidade_base = models.CharField(max_length=6, blank=True, null=True)
    tp_unidade_base = models.CharField(max_length=12, blank=True, null=True)
    dc_unidade_base = models.CharField(max_length=60, blank=True, null=True)
    sigla_lotacao = models.TextField(blank=True, null=True)
    tp_lotacao = models.CharField(max_length=1, blank=True, null=True)
    cd_cargo_atual = models.IntegerField(blank=True, null=True)
    dc_cargo_atual = models.CharField(max_length=70, blank=True, null=True)
    cd_area_atuacao_cargo_atual = models.IntegerField(blank=True, null=True)
    dc_area_atuacao_cargo_atual = models.CharField(max_length=70, blank=True, null=True)
    cd_unidade_educacao_atual = models.CharField(max_length=6, blank=True, null=True)
    tp_unidade_educacao_atual = models.CharField(max_length=50, blank=True, null=True)
    dc_unidade_educacao_atual = models.CharField(max_length=60, blank=True, null=True)
    sigla_atual = models.TextField(blank=True, null=True)
    cd_unidade_funcao = models.CharField(max_length=20, blank=True, null=True)
    cd_funcao = models.IntegerField(blank=True, null=True)
    dc_funcao = models.CharField(max_length=100, blank=True, null=True)
    dt_inicio_funcao = models.TextField(blank=True, null=True)
    cd_unidade_sobreposto = models.CharField(max_length=20, blank=True, null=True)
    cd_sobreposto = models.IntegerField(blank=True, null=True)
    dc_sobreposto = models.CharField(max_length=100, blank=True, null=True)
    dt_inicio_sobreposto = models.TextField(blank=True, null=True)
    database = models.TextField(blank=True, null=True)
