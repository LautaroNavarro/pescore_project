from django import forms
from Apps.competencia.models import Campeonato,Torneo,Categoria,Club,Especialidad,Participante,Tarjeta, Torneo
class ClubForm (forms.ModelForm):
	class Meta:
		model = Club
		fields = '__all__'
		labels = {'nombre' : 'Nombre',
			      'abreviacion' : 'Abreviacion',
		}
		widgets = {'nombre' : forms.TextInput(attrs = {'class' : 'form-control'}),
				   'abreviacion' : forms.TextInput(attrs = {'class' : 'form-control'}),
		}

class CategoriaForm (forms.ModelForm):
	class Meta:
		model = Categoria
		fields = '__all__'
		labels = {'nombre' : 'Nombre',
				  }
		widgets = {'nombre' : forms.TextInput(attrs = {'class' : 'form-control'}),
		}
class ParticipanteForm(forms.ModelForm):
	class Meta:
		model = Participante
		fields = '__all__'
		labels = {'nombre': 'Nombre',
			      'apellido' : 'Apellido',
				  'fechaNacimiento' : 'Fecha de Nacimiento',
				  'club' : 'Club',
				  'categoria' : 'Cateogoria',
		}
		widgets = {'nombre': forms.TextInput(attrs = {'class' : 'form-control'}),
			      'apellido' : forms.TextInput(attrs = {'class' : 'form-control'}),
				  'fechaNacimiento' : forms.TextInput( attrs = {'class' : 'form-control', 'type' : 'Date'}),
				  'club' : forms.Select(attrs = {'class' : 'form-control'} ,choices = Club.objects.all()),
				  'categoria' : forms.Select(attrs = {'class' : 'form-control'}, choices = Categoria.objects.all()),
		}

class EspecialidadForm (forms.ModelForm):
	class Meta:
		model = Especialidad
		fields = '__all__'
		labels = {'nombre' : 'Nombre',
				  'descripcion' : 'Descripcion'}
		widgets = {'nombre' : forms.TextInput(attrs = {'class' : 'form-control'}),
				  'descripcion' : forms.TextInput(attrs = {'class' : 'form-control'})}

class CampeonatoForm (forms.ModelForm):
	class Meta:
		model = Campeonato
		fields = '__all__'
		labels = {'fecha' : 'Fecha',
				  'nombre' : 'Nombre',
				  'cantidadPescadores' : 'Cantidad de pescadores',
				  'cantidadClubes' : 'Cantidad de clubes',
				  'participantes' : 'Participantes'}
		widgets = {'fecha' : forms.DateInput(attrs = {'class' : 'form-control', 'type' : 'date'}),
				  'nombre' : forms.TextInput(attrs = {'class' : 'form-control'}),
				  'cantidadPescadores' : forms.NumberInput(attrs = {'class' : 'form-control'}),
				  'cantidadClubes' : forms.NumberInput(attrs = {'class' : 'form-control'}),
				  'participantes' : forms.SelectMultiple(attrs = {'class' : 'form-control'})}


class TorneoForm (forms.ModelForm):
	class Meta:
		model = Torneo
		fields = '__all__'
		labels = {'fecha' : 'Fecha',
				  'campeonato' : 'Campeonato',
				  'especilidad' : 'Especialidad',
				  'club' : 'Club'
		}
		widgets = {'fecha' : forms.DateInput(attrs = {'class' : 'form-control', 'type' : 'date'}),
				  'campeonato' : forms.Select(attrs = {'class' : 'form-control'}),
				  'especilidad' : forms.Select(attrs = {'class' : 'form-control'}),
				  'club' : forms.Select(attrs = {'class' : 'form-control'}),
		}

class TarjetaForm (forms.Form):
	cantidad = forms.IntegerField(label = 'Cantidad')
	peso = forms.IntegerField(label = 'Peso')
	hora = forms.TimeField(label = 'Hora')
	torneo = forms.ChoiceField(label = 'Torneo', choices = Torneo.objects.all())
	participante = forms.ChoiceField(label = 'Participante' , choices = Participante.objects.all())
	class Meta:
		model = Tarjeta

