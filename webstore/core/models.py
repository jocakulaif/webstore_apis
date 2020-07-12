from django.db import models

# Create your models here.


class Product(models.Model):
    barcode = models.CharField(max_length=120, verbose_name='Codigo de Barra', unique=True)
    product = models.CharField(max_length=100, verbose_name='Produto')
    description = models.CharField(max_length=120, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.product}'

    class Meta:
        managed = True
        verbose_name_plural = 'Produtos'
        db_table = 'products'


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    lastname = models.CharField(max_length=50, verbose_name='Sobrenome')
    contact_no = models.CharField(max_length=25, verbose_name='Contato')
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, verbose_name='Ativo')

    def __str__(self):
        return f'{self.name} {self.lastname}'

    class Meta:
        verbose_name_plural = 'Clientes'
        db_table = 'client'
        managed = True
