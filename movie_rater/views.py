from django.shortcuts import render
from . models import Movie
from django.utils import timezone

# Create your views here.
def movie_list(request):
	movies = Movie.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'movie_rater/movie_list.html', {'movies':movies})
