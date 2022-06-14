from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    usernamet = models.CharField(max_length=100)
    campeonatos =models.ManyToManyField('Campeonato', through='Campeonato_equipo')


    def __str__(self):
        return "%s - %s - %s" % (self.nombre, 
                self.siglas, self.usernamet)

# nombre, posición campo, número camiseta, sueldo, equipo de fútbol
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion_campo = models.CharField(max_length=50)
    num_camiseta = models.CharField(max_length=100)
    sueldo = models.IntegerField("sueldo del jugador")
    equipo = models.ForeignKey('Equipo', related_name='jugadores', 
            on_delete=models.CASCADE)


    def __str__(self):
        return "%s - %s - %s - %d" % (self.nombre, 
                self.posicion_campo,
                self.num_camiseta,
                self.sueldo,)

# Campeonato: nombre de campeonato, nombre de auspiciante

class Campeonato(models.Model):
    nombre_campeonato = models.CharField(max_length=100)
    nombre_auspiciante = models.CharField(max_length=100)
    equipos =models.ManyToManyField('Equipo', through='Campeonato_equipo')



    def __str__(self):
        return "%s - %s" % (self.nombre_campeonato, 
                self.nombre_auspiciante)

#Campeonato Equipos: año, equipo de fútbol, campeonato
class Campeonato_equipo(models.Model):
    anio = models.IntegerField("año campeonato")
    equipo = models.ForeignKey(Equipo, related_name='campeonatos_eq', 
            on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='campeonatos_eq', 
        on_delete=models.CASCADE)

    def __str__(self):
        return "%d" % (self.anio)
