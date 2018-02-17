from django.shortcuts import get_object_or_404, render

from .models import *


def index(request):
    movies = Movie.objects.all()
    tags = Tag.objects.all()
    return render(request, 'index.html', {
        'movies': movies,
        'tags': tags
    })


def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'detail.html', {
        'movie': movie
    })
