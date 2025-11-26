from cursos import views
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r"cursos", views.CursosViewSet, basename="curso")

urlpatterns = [
    path(
        "reportes/horas-semanales/",
        views.reporte_horas_semanales,
        name="reporte-horas-semanales",
    ),
]

urlpatterns += router.urls
