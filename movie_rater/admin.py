from django.contrib import admin
from .models import Movie
from .models import Person
from .models import MovieRating

admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(MovieRating)
