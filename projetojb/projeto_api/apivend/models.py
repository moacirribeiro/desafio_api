from django.db import models

class Vendedores(models.Model):
    nome_vendedor = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=1)

    def __str__(self):
        return self.nome_vendedor

class Cidades(models.Model):
    uf = models.CharField(max_length=2)
    nome_cidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_cidade

class VendedoresCidades(models.Model):
    cod_vendedor = models.ForeignKey(Vendedores, on_delete=models.CASCADE)
    cod_cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)

    def __str__(self):
        return self.cod_cidade + ": " + self.cod_vendedor
