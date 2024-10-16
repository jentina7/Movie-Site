from django_filters import FilterSet
from .models import Movie


class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            "country": ["exact"],
            "year": ["gt", "lt"],
            "genre": ["exact"],
            "movie_status": ["exact"],
            "actor": ["exact"],
            "director": ["exact"]
        }