from django.db import models

class Login(models.Model):
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.nome, self.senha)
    
class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    nome_de_usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    culinarias_preferidas = models.ManyToManyField('Culinaria')

    def __str__(self):
        return self.nome_de_usuario

class Culinaria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome