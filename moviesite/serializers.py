from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("username", "email", "password", "first_name", "last_name", "age",
                  "date_registered", "phone_number", "status")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only= True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            "user": {
                "username": instance.username,
                "email": instance.email,
            },
            'access': str(refresh.access_token),
            "refresh": str(refresh),
        }



class HistorySerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    class Meta:
        model = History
        fields = ['user', 'movie', 'date']


class ProfileSerializer(serializers.ModelSerializer):
    view_history = HistorySerializer()
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name"]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["country_name"]


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ["director", "director_image"]


class ActorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["actor", "actor_image"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["genre"]


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ["languages", "video"]


class RatingSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    user = ProfileSimpleSerializer(read_only=True)
    movie = serializers.SlugRelatedField(slug_field="movie_name", queryset=Movie.objects.all())

    class Meta:
        model = Rating
        fields = ["user", "movie", "stars", "text", "parent", "created_date"]



class MovieSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    genre = GenreSerializer(read_only=True, many=True)
    actor = ActorSerializer(read_only=True, many=True)
    director = DirectorSerializer(read_only=True, many=True)
    languages = MovieLanguagesSerializer(read_only=True, many=True)
    ratings = RatingSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["movie_name", "movie_image", "year", "country", "genre", "actor", "director", "types",
                  "movie_time", "description", "movie_trailer", "languages", "ratings", "average_rating", "movie_status"]

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class MovieListSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    genre = GenreSerializer(read_only=True, many=True)
    actor = ActorSerializer(read_only=True, many=True)
    director = DirectorSerializer(read_only=True, many=True)
    languages = MovieLanguagesSerializer(read_only=True, many=True)
    class Meta:
        model = Movie
        fields = ["movie_name", "movie_image", "year", "country", "genre", "actor", "director", "types",
                  "movie_time", "description", "movie_trailer", "languages", "movie_status"]


class MomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moment
        fields = ["movie", "movie_moment"]


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = "__all__"

