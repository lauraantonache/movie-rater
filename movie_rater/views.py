from django.shortcuts import render

# Create your views here.
def movie_list(request):
	return render(request, 'movie_rater/movie_list.html', {})
