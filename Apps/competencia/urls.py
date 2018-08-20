from django.urls import path
from Apps.competencia.views import (landingPage, 
									AltaClub, 
									ListarClubes, 
									ListarCategorias, 
									AltaCategoria,
									ListarParticipantes,
									AltaParticipante,
                                    ListarEspecialidades,
                                    AltaEspecialidad)

app_name = 'competencia'
urlpatterns = [
    path('landingPage/',landingPage, name = 'landingPage'),
    path('club/alta/', AltaClub.as_view()),
    path('club/listar/', ListarClubes.as_view()),
    path('categoria/listar/', ListarCategorias.as_view()),
    path('categoria/alta/' , AltaCategoria.as_view()),
    path('participante/listar/' , ListarParticipantes.as_view()),
    path('participante/alta/', AltaParticipante.as_view()),
    path('especialidad/listar/' , ListarEspecialidades.as_view()),
    path('especialidad/alta/', AltaEspecialidad.as_view()),
]