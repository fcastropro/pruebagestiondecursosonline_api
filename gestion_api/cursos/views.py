from rest_framework import viewsets, filters
from cursos.models import Cursos
from cursos.serializers import CursosSerializer

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("titulo","subtitulo")
    ordering_fields = ("titulo","created_at")