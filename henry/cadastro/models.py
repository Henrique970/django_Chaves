from django.db import models


class Chave(models.Model):
    nome = models.CharField(max_length=100)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

#class Imprestimo(models.Model):
#    nome = models.CharField(max_length=100)
#    hr_pego = models.CharField(max_length=100)
#    hr_devolvido = models.CharField(max_length=100)





