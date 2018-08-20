from django.shortcuts import render
from django.views.generic import ListView, CreateView
from Apps.competencia.models import Club, Categoria, Participante, Especialidad, Campeonato
from Apps.competencia.forms import ClubForm, CategoriaForm, CampeonatoForm, ParticipanteForm, EspecialidadForm
from django.urls import reverse
# Create your views here.
def landingPage(request):
	return render(request,'Competencia/landingPage.html')

class ListarClubes (ListView):
	model = Club
	template_name = 'Competencia/club/listar.html'
class AltaClub (CreateView):
	model = Club
	form_class = ClubForm
	template_name = 'Competencia/club/alta.html'
	#fields = ['nombre','abreviacion']
	success_url = '/club/listar/'

class ListarCategorias (ListView):
	model = Categoria
	template_name = 'Competencia/categoria/listar.html'
class AltaCategoria (CreateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'Competencia/categoria/alta.html'
	success_url = '/categoria/listar/'

class ListarParticipantes (ListView):
	model = Participante
	template_name = 'Competencia/participante/listar.html'
class AltaParticipante (CreateView):
	model = Participante
	form_class = ParticipanteForm
	template_name = 'Competencia/participante/alta.html'
	success_url = '/participante/listar/'
class ListarEspecialidades (ListView):
	model = Especialidad
	template_name = 'Competencia/especialidad/listar.html'
class AltaEspecialidad(CreateView):
	model = Especialidad
	form_class = EspecialidadForm
	template_name = 'Competencia/especialidad/alta.html'
	success_url = '/especialidad/listar/'
class AltaCampeonato(CreateView):
	model = Campeonato
	form_class = CampeonatoForm
	template_name = 'Competencia/campeonato/alta.html'
	success_url = '/campeonato/listar/'
class ListarCampeonatos(ListView):
	model = Campeonato
	template_name = 'Competencia/campeonato/listar.html'