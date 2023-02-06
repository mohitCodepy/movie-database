from rest_framework import serializers

from movies_and_cast.models import Cast, Movie


class MovieAllSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format="iso-8601")
    updated_at = serializers.DateTimeField(read_only=True, format="iso-8601")

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "language",
            "tagline",
            "created_at",
            "updated_at",
        )


class MovieSingleReadOnlySerializer(serializers.ModelSerializer):
    cast = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, format="iso-8601")
    updated_at = serializers.DateTimeField(read_only=True, format="iso-8601")

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "language",
            "tagline",
            "created_at",
            "updated_at",
            "cast",
        )

    def get_cast(self, obj):
        return MovieCastSerializer(obj.movie_casts.all(), many=True).data


class CastCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ("id", "name", "gender", "dob", "movie")


class MovieCastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ("id", "name", "gender", "dob")
