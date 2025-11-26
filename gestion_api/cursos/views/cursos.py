# cursos/views.py

from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cursos.models import Cursos
from cursos.serializers import CursosSerializer


class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("titulo", "subtitulo")
    ordering_fields = ("titulo", "created_at")


@api_view(["POST"])
def reporte_horas_semanales(request):
    horas = request.data.get("horasPorDia")

    if horas is None:
        return Response(
            {"error": "El campo 'horasPorDia' es requerido."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not isinstance(horas, list):
        return Response(
            {"error": "'horasPorDia' debe ser un arreglo (lista) de números."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if len(horas) != 7:
        return Response(
            {"error": "'horasPorDia' debe tener exactamente 7 valores (uno por día)."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    total_horas = 0.0
    for valor in horas:
        try:
            total_horas += float(valor)
        except (TypeError, ValueError):
            return Response(
                {"error": "Todos los elementos de 'horasPorDia' deben ser numéricos."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    promedio = total_horas / 7.0

    if promedio < 1:
        mensaje = "Estás estudiando muy poco"
    elif promedio <= 3:
        mensaje = "Buen ritmo de estudio"
    else:
        mensaje = "Excelente dedicación"

    data = {
        "totalHoras": round(total_horas, 2),
        "promedio": round(promedio, 2),
        "mensaje": mensaje,
    }

    return Response(data, status=status.HTTP_200_OK)
