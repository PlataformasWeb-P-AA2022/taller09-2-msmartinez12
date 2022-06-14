from django.contrib import admin

# Importar las clases del modelo
from futbolec.models import Equipo, Jugador, Campeonato, Campeonato_equipo


class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion_campo', 'num_camiseta', 'sueldo', 'equipo')
    search_fields = ('nombre', 'equipo__nombre')

admin.site.register(Jugador, JugadorAdmin)

admin.site.register(Equipo)
admin.site.register(Campeonato)


# admin.site.register(Matricula)
class Campeonato_equipoAdmin(admin.ModelAdmin):

    list_display = ('anio', 'equipo', 'campeonato')
    search_fields = ('equipo__nombre', 'anio', 'campeonato__nombre_campeonato')

admin.site.register(Campeonato_equipo, Campeonato_equipoAdmin)

