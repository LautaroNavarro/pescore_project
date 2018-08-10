from django.db import models

# Create your models here.
class Club (models.Model):
	nombre = models.CharField(max_length = 50)
	abreviacion = models.CharField(max_length = 3)
	def __str__(self):
		return self.nombre

class Categoria (models.Model):
	nombre = models.CharField(max_length = 50)
	def __str__(self):
		return self.nombre

class Participante (models.Model):
	nombre =  models.CharField(max_length = 50)
	apellido =  models.CharField(max_length = 50)
	fechaNacimiento = 	models.DateField()
	club = models.ForeignKey(Club, null = False, blank = False, on_delete = models.CASCADE)
	categoria = models.ForeignKey(Categoria, null = False, blank = False, on_delete = models.CASCADE)
	def __str__(self):
		return self.nombre + " " + self.apellido



class Especialidad (models.Model):
	nombre = models.CharField(max_length = 50)
	descripcion = models.TextField()
	def __str__(self):
		return self.nombre
class Campeonato (models.Model):
	fecha = models.DateField()
	nombre = models.CharField(max_length = 50)
	cantidadPescadores = models.IntegerField()
	cantidadClubes = models.IntegerField()
	participantes = models.ManyToManyField(Participante)
	def __str__(self):
		return self.nombre
	def getRankingGeneralIndividual():
		return null
	def getRankingGeneralClub():
		return null

class Torneo (models.Model):
	fecha = models.DateField()
	campeonato = models.ForeignKey(Campeonato, null = False, blank = False, on_delete = models.CASCADE)
	especialidad = models.ForeignKey(Especialidad, null = False, blank = False, on_delete = models.CASCADE)
	club = models.ForeignKey(Club, null = False, blank = False, on_delete = models.CASCADE)
	def __str__(self):
		return self.campeonato.nombre + " " + self.fecha.strftime('%m/%d/%Y')
	def getRankingIndividual():
		return null
	def getRankingClub():
		return null
class Tarjeta (models.Model):
	cantidad = models.IntegerField()
	peso = 	models.FloatField()
	hora = 	models.TimeField()
	puntaje = models.FloatField()
	torneo = models.ForeignKey(Torneo, null = False, blank = False, on_delete = models.CASCADE)
	participante = models.ForeignKey(Participante, null = False, blank = False, on_delete = models.CASCADE)
	def __str__(self):
		return self.participante.nombre + " " +  self.participante.id