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
@api_view(["POST"])
def evaluacion_aprobacion(request):

    notas = request.data.get("notas")
    nota_minima = request.data.get("notaMinima")

    if notas is None or nota_minima is None:
        return Response(
            {"error": "Los campos 'notas' y 'notaMinima' son requeridos."},
            status=status.HTTP_400_BAD_REQUEST
        )

    if not isinstance(notas, list):
        return Response(
            {"error": "'notas' debe ser un arreglo (lista) de números."},
            status=status.HTTP_400_BAD_REQUEST
        )

    if len(notas) < 3 or len(notas) > 5:
        return Response(
            {"error": "'notas' debe tener entre 3 y 5 valores."},
            status=status.HTTP_400_BAD_REQUEST
        )

    total = 0.0
    for n in notas:
        try:
            total += float(n)
        except (TypeError, ValueError):
            return Response(
                {"error": "Todos los valores de 'notas' deben ser numéricos."},
                status=status.HTTP_400_BAD_REQUEST
            )

    promedio = total / len(notas)

    if promedio >= float(nota_minima):
        estado = "Aprobado"
        mensaje = f"El estudiante aprobó con promedio {promedio:.2f}."
    else:
        estado = "Reprobado"
        mensaje = f"El estudiante reprobó con promedio {promedio:.2f}."

    data = {
        "promedio": round(promedio, 2),
        "estado": estado,
        "mensaje": mensaje
    }

    return Response(data, status=status.HTTP_200_OK)
