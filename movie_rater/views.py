from django.shortcuts import render, get_object_or_404, redirect
from . models import Movie
from . forms import MovieForm
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def movie_list(request):
	movies = Movie.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'movie_rater/movie_list.html', {'movies':movies})
	
def movie_detail(request, pk):
	movie = get_object_or_404(Movie, pk=pk)
	return render(request, 'movie_rater/movie_detail.html', {'movie': movie})
	
def new_movie(request):
	if request.method == "POST":
		form = MovieForm(request.POST)
		if form.is_valid():
			if request.user.is_authenticated():
				movie = form.save(commit=False)
				movie.author = request.user
				movie.created_date = timezone.now()
				movie.save()
				return redirect('movie_rater.views.movie_detail', pk=movie.pk)
	else:
		form = MovieForm()
	return render(request, 'movie_rater/movie_edit.html', {'form': form})
	

def login_view(request, ):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('movie_rater.views.new_movie')
        else:
            return redirect('movie_rater.views.login_view')
    else:
         return redirect('movie_rater.views.login_view')
