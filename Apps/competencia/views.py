from django.shortcuts import render
from django.views.generic import ListView, CreateView
from Apps.competencia.models import Club
from Apps.competencia.forms import ClubForm
from django.urls import reverse
# Create your views here.
def landingPage(request):
	return render(request,'Competencia/landingPage.html')
class ListarClubes (ListView):
	model = Club
	template_name = 'Competencia/listarClubes.html'
class AltaClub (CreateView):
	model = Club
	form_class = ClubForm
	template_name = 'Competencia/altaClub.html'
	#fields = ['nombre','abreviacion']
	success_url = '/listarClubes/'

