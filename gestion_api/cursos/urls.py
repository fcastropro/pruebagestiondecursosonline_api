# cursos/urls.py
from rest_framework.routers import DefaultRouter

from cursos.views import CursosViewSet

router = DefaultRouter()
router.register(r"cursos", CursosViewSet, basename="curso")

urlpatterns = router.urls
