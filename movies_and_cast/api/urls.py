from rest_framework.routers import DefaultRouter

from movies_and_cast.api.views import CastViewSet, MovieViewSet

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"casts", CastViewSet, basename="cast")

urlpatterns = router.urls
