from django.db import models

# Create your models here.


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    celular = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    codigo = models.CharField(max_length=20)

    def __str__(self):
        return self.nome