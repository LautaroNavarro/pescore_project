from django.urls import path
from Apps.competencia.views import landingPage 
# 									AltaClub, 
# 									ListarClubes, 
# 									ListarCategorias, 
# 									AltaCategoria,
# 									ListarParticipantes,
# 									AltaParticipante,
#                                     ListarEspecialidades,
#                                     AltaEspecialidad,
#                                     ListarCampeonatos,
#                                     AltaCampeonato,
#                                     ListarTorneos,
#                                     AltaTorneo,
#                                     AltaTarjeta,
#                                     ListarTarjetas)

# app_name = 'competencia'
urlpatterns = [
    path('landingPage/',landingPage, name = 'landingPage'),
#     path('club/alta/', AltaClub.as_view()),
#     path('club/listar/', ListarClubes.as_view()),
#     path('categoria/listar/', ListarCategorias.as_view()),
#     path('categoria/alta/' , AltaCategoria.as_view()),
#     path('participante/listar/' , ListarParticipantes.as_view()),
#     path('participante/alta/', AltaParticipante.as_view()),
#     path('especialidad/listar/' , ListarEspecialidades.as_view()),
#     path('especialidad/alta/', AltaEspecialidad.as_view()),
#     path('campeonato/listar/' , ListarCampeonatos.as_view()),
#     path('campeonato/alta/', AltaCampeonato.as_view()),
#     path('torneo/listar/' , ListarTorneos.as_view()),
#     path('torneo/alta/', AltaTorneo.as_view()),
#     path('tarjeta/listar/' , ListarTarjetas.as_view()),
#     path('tarjeta/alta/', AltaTarjeta.as_view()),
]