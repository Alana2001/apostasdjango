from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Sorteio(models.Model):
    concurso = models.CharField(max_length=4)
    primeiro_animal = models.CharField(max_length=30)
    segundo_animal = models.CharField(max_length=30)
    data_sorteio = models.DateTimeField(default=timezone.now)
    
    def fazsorteio(self):
        self.data_sorteio = timezone.now()
        self.save()

    def __str__(self):
        return self.concurso

class Aposta(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    primeiro_animal = models.CharField(max_length=30)
    segundo_animal = models.CharField(max_length=30)
    data_aposta = models.DateTimeField(default=timezone.now)
    concurso = models.OneToOneField(Sorteio, on_delete=models.SET_NULL, null=True)
    

    def dataaposta(self):
        self.data_aposta= timezone.now()
        self.save()



class Apostador(models.Model):
    nome = models.CharField(max_length=200)
    saldo = models.FloatField()

    def __str__(self):
        return self.nome
