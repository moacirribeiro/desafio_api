from rest_framework import serializers
from .models import Vendedores, Cidades, VendedoresCidades

class VendedoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendedores 
        fields = ['id', 'nome_vendedor', 'email', 'status']

class CidadesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidades
        fields = ['id', 'uf', 'nome_cidade']

class VendedoresCidadesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VendedoresCidades
        fields = ['cod_vendedor', 'cod_cidade']