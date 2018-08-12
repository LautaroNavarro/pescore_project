from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def LandingPage(request):
	return render(request,'Competencia/landingPage.html')