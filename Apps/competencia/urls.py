from django.urls import path
from Apps.competencia.views import landingPage, AltaClub, ListarClubes
from Apps.competencia.models import Club

app_name = 'competencia'
urlpatterns = [
    path('landingPage/',landingPage, name = 'landingPage'),
    path('altaClub/', AltaClub.as_view()),
    path('listarClubes/', ListarClubes.as_view()),
]