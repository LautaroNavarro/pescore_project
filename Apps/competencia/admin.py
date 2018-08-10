from django.contrib import admin
from Apps.competencia.models import Club, Categoria, Participante, Campeonato, Especialidad, Tarjeta, Torneo
# Register your models here.
admin.site.register(Club)
admin.site.register(Categoria)
admin.site.register(Participante)
admin.site.register(Campeonato)
admin.site.register(Especialidad)
admin.site.register(Tarjeta)
admin.site.register(Torneo)