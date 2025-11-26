from rest_framework import serializers
from cursos.models import Cursos

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = ("id","codigo","titulo","subtitulo","descripcion","nivel","duracion_horas","costo","modalidad","fecha_inicio","created_at","updated_at")
        read_only_fields = ("id","created_at","updated_at")