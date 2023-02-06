from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from movies_and_cast.api.serializers import (CastCreateSerializer,
                                             MovieAllSerializer,
                                             MovieSingleReadOnlySerializer)
from movies_and_cast.exceptions import MovieNotExistsException
from movies_and_cast.models import Cast, Movie


class MovieViewSet(ModelViewSet):

    http_method_names = ['get', 'post']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Movie.objects.prefetch_related("movie_casts")
    serializer_class = MovieAllSerializer

    def retrieve(self, request, pk, *args, **kwargs):
        try:
            movie = get_object_or_404(Movie, pk=pk)
        except Exception as e:
            raise MovieNotExistsException({"error": "movie doesn't exist"})

        serializer = MovieSingleReadOnlySerializer(movie)
        return Response(serializer.data, status=HTTP_200_OK)


class CastViewSet(ModelViewSet):
    http_method_names = ['get', 'post']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Cast.objects.select_related("movie")
    serializer_class = CastCreateSerializer
