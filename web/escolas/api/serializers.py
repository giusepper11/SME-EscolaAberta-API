from rest_framework.serializers import ModelSerializer, SerializerMethodField
from escolas.models import Escolas, Ceus


class EscolasSerializer(ModelSerializer):
    class Meta:
        model = Escolas
        fields = (
            '__all__'
        )
        # filter_fields = ('cdesc')
        filter_fields = ('codesc')


class BairroSerializer(ModelSerializer):
    class Meta:
        model = Escolas
        fields = ('bairro',)
        filter_fields = ('bairro',)


class DistritoSerializer(ModelSerializer):
    class Meta:
        model = Escolas
        fields = ('distrito',)
        filter_fields = ('distrito',)


class SubprefSerializer(ModelSerializer):
    class Meta:
        model = Escolas
        fields = ('subpref',)
        filter_fields = ('subpref',)


class CeuSerializer(ModelSerializer):
    dre = SerializerMethodField('get_nm_unidade_administrativa')

    class Meta:
        model = Ceus
        fields = ('cd_unidade', 'nm_unidade', 'nm_exibicao_unidade', 'tp_unidade_administrativa',
                  'dc_tipo_unidade_administrativa', 'sg_unidade_administrativa',
                  'cd_unidade_administrativa', 'dre')

    def get_nm_unidade_administrativa(self, obj):
        return obj.nm_unidade_administrativa.replace('DRE - ', '')
