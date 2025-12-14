from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    cpf =  models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=False)
    assinatura_valida = models.BooleanField(default=False)
    imagem_assinatura = models.ImageField(upload_to='assinaturas/', null=True, blank=True)
    hash_integridade = models.CharField(max_length=64, blank=True)