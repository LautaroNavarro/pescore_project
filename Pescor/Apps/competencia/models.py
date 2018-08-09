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

