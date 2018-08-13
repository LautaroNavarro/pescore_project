from django.urls import path
from Apps.competencia.views import landingPage

app_name = 'competencia'
urlpatterns = [
    path('landingPage/',landingPage, name='landingPage'),
]