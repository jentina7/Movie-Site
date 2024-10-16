from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("", MovieListViewSet.as_view({"get": "list"}), name = "movie_list"),
    path("<int:pk>/", MovieViewSet.as_view({"get": "retrieve"}), name = "movie_detail"),

    path("country", CountryViewSet.as_view({"get": "list"}), name="country_list"),
    path("country/<int:pk>/", CountryViewSet.as_view({"get": "retrieve"}), name="country_detail"),

    path("genre", GenreViewSet.as_view({"get": "list"}), name="genre_list"),
    path("genre/<int:pk>/", GenreViewSet.as_view({"get": "retrieve"}), name="genre_detail"),

    path("actor", ActorViewSet.as_view({"get": "list"}), name="actor_list"),
    path("actor/<int:pk>/", ActorDetailViewSet.as_view({"get": "retrieve"}), name="actor_detail"),

    path("director", DirectorViewSet.as_view({"get": "list"}), name="director_list"),
    path("director/<int:pk>/", DirectorDetailViewSet.as_view({"get": "retrieve"}), name="director_detail"),

    path("moment", MomentViewSet.as_view({"get": "list"}), name="moment_list"),
    path("moment/<int:pk>/", MomentViewSet.as_view({"get": "retrieve"}), name="moment_detail"),

    path("profile", ProfileViewSet.as_view({"get": "list"}), name="profile_list"),
    path("profile/<int:pk>/", ProfileViewSet.as_view({"get": "retrieve"}), name="profile_detail"),

    path("languages", MovieLanguagesViewSet.as_view({"get": "list"}), name="languages_list"),
    path("languages/<int:pk>/", MovieLanguagesViewSet.as_view({"get": "retrieve"}), name="languages_detail"),

    path("rating", RatingViewSet.as_view({"get": "list"}), name="rating_list"),
    path("rating/<int:pk>/", RatingViewSet.as_view({"get": "retrieve"}), name="rating_detail"),

    path("favorite",FavoriteViewSet.as_view({"get": "list"}), name="favorite_list"),
    path("favorite/<int:pk>/", FavoriteViewSet.as_view({"get": "retrieve"}), name="favorite_detail"),

    path("favorite_movie", FavoriteMovieViewSet.as_view({"get": "list"}), name="favorite_movie_list"),
    path("favorite_movie/<int:pk>/", FavoriteMovieViewSet.as_view({"get": "retrieve"}), name="favorite_movie_detail"),

    path("history", HistoryViewSet.as_view({"get": "list"}), name="history_list"),
    path("history/<int:pk>/", HistoryViewSet.as_view({"get": "retrieve"}), name="history_detail"),


]