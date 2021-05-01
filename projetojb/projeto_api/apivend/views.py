from django.shortcuts import render
from rest_framework import viewsets
from .models import Vendedores, Cidades, VendedoresCidades
from .serializers import VendedoresSerializer, CidadesSerializer, VendedoresCidadesSerializer

class VendedoresView(viewsets.ModelViewSet):
    queryset = Vendedores.objects.all()
    serializer_class = VendedoresSerializer

class CidadesView(viewsets.ModelViewSet):
    queryset = Cidades.objects.all()
    serializer_class = CidadesSerializer

class VendedoresCidadesView(viewsets.ModelViewSet):
    queryset = VendedoresCidades.objects.all()
    serializer_class = VendedoresCidadesSerializer