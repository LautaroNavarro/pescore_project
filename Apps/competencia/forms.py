from django import forms
from Apps.competencia.models import Campeonato,
								    Categoria,
								    Club, 
								    Especialidad, 
								    Participante, 
								    Tarjeta
class ClubForm (forms.Form):
	nombre = forms.CharField(label = 'Nombre' , max_lenght = 50)
	abreviacion = forms.CharField(label = 'Abreviacion' , max_lenght = 3)
	class Meta:
		model = Club
class CategoriaForm (forms.Form):
	nombre = forms.CharField(label = 'Nombre', max_lenght = 50)
	class Meta:
		model = Categoria
class ParticipanteForm (forms.Form):
	nombre = forms.CharField(label = 'Nombre', max_lenght = 50)
	apellido = forms.CharField(label = 'Apellido', max_lenght = 50)
	fechaNacimiento = forms.DateField(label = 'Fecha Nacimiento')
	club = forms.ChoiceField(label = 'Club', choices = Club.objects.all())
	class Meta:
		model = Participante
class EspecialidadForm (forms.Form):
	nombre = forms.CharField(label = 'Nombre', max_lenght = 50)
	nombre = forms.CharField(label = 'Nombre', max_lenght = 50)
	class Meta:
		model = Especialidad
class CampeonatoForm (forms.Form):
	fecha = forms.DatField(label = 'Fecha')
	nombre = forms.CharField(label = 'Nombre', max_lenght = 50)
	cantidadPescadores = forms.IntegerField(label = 'Cantidad de Pescadores')
	cantidadClubes = forms.IntegerField(label = 'Cantidad de Clubes')
	participantes = forms.TypedMultipleChoiceField(label = 'Participantes', choices = Participante.objects.all())
	class Meta:
		model = Campeonato
class TorneoForm (forms.Form):
	fecha = forms.DatField(label = 'Fecha')
	campeonato = forms.ChoiceField(label = 'Campeonato', choices = Campeonato.objects.all())
	especilidad = forms.ChoiceField(label = 'Especialidad', choices = Especialidad.objects.all())
	club = forms.ChoiceField(label = 'Club', choices = Club.objects.all())
	class Meta:
		model = Campeonato
class TarjetaForm (forms.Form):
	cantidad = forms.IntegerField(label = 'Cantidad')
	peso = forms.IntegerField(label = 'Peso')
	hora = forms.TimeField(label = 'Hora' blank=True)
	torneo = forms.ChoiceField(label = 'Torneo', choices = Torneo.objects.all())
	participante = forms.ChoiceField(label = 'Participante' , choices = Participante.objects.all())
	class Meta:
		model = Tarjeta

