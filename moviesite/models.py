from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18),
                                                       MaxValueValidator(100)])
    phone_number = PhoneNumberField(null=True, blank=True, region="KG")
    date_registered = models.DateField(auto_now=True, null=True, blank=True)
    STATUS_CHOICES = (
        ("pro", "Pro"),
        ("simple", "Simple")
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="simple", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Country(models.Model):
    country_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director = models.CharField(max_length=16, unique=True)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18),
                                                       MaxValueValidator(100)])
    director_image = models.ImageField(upload_to="image")

    def __str__(self):
        return self.director


class Actor(models.Model):
    actor = models.CharField(max_length=16)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18),
                                                       MaxValueValidator(100)])
    actor_image = models.ImageField(upload_to="image")

    def __str__(self):
        return self.actor


class Genre(models.Model):
    genre = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.genre


class MovieLanguages(models.Model):
    languages = models.CharField(max_length=32, unique=True)
    video = models.FileField(upload_to="video")


class Movie(models.Model):
    movie_name = models.CharField(max_length=32, unique=True)
    year = models.DateField(auto_now=False)
    country = models.ForeignKey(Country, related_name="movie_country", on_delete=models.CASCADE)
    director = models.ManyToManyField(Director, related_name="movie_director")
    actor = models.ManyToManyField(Actor, related_name="movie_actor")
    genre = models.ManyToManyField(Genre, related_name="movie_genre")
    MOVIE_TYPES_CHOICES = (
        ("144", "144"),
        ("360", "360"),
        ("480", "480"),
        ("720", "720"),
        ("1080", "1080")
    )

    types = MultiSelectField(max_length=5, choices=MOVIE_TYPES_CHOICES, max_choices=5)
    movie_time = models.SmallIntegerField(default=0)
    description = models.TextField()
    movie_trailer = models.FileField(upload_to="trailer", null=True, blank=True)
    movie_image = models.ImageField(upload_to="image")
    movie = models.ManyToManyField(MovieLanguages)
    MOVIE_STATUS_CHOICES = (
        ("pro", "Pro"),
        ("simple", "Simple")
    )
    movie_status = models.CharField(max_length=10, choices=MOVIE_STATUS_CHOICES, default="simple", null=True,
                                    blank=True)

    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0

    def __str__(self):
        return self.movie_name


class Moment(models.Model):
    movie = models.ForeignKey(Movie, related_name="moment", on_delete=models.CASCADE)
    movie_moment = models.ImageField(upload_to="image")


class Rating(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="ratings", on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 10)], verbose_name="Рейтинг", null=True,
                                blank=True)
    parent = models.ForeignKey("self", related_name="replies", null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie} - {self.user} - {self.stars} stars"


class Favorite(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="favorite")
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"


class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, related_name="cart", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class History(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="view_history")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="viewed_movie")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} watched {self.movie} on {self.date}"