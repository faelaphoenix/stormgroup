from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, Cast, Genre


def movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'managerfilms/movie_list.html', context)


class CastList(ListView):
    template_name = 'managerfilms/cast_list.html'
    model = Cast
    context_object_name = 'casts'

    def get_queryset(self):
        c = Cast.objects.all()
        return c


class MovieList(ListView):
    template_name = 'managerfilms/movie_list.html'
    model = Movie
    context_object_name = 'movies'

    def get_queryset(self):
        m = Movie.objects.all()
        return m


class MovieDetail(DetailView):
    template_name = 'managerfilms/movie_detail.html'
    model = Movie


class GenreDetail(DetailView):
    template_name = 'managerfilms/genre_detail.html'
    model = Genre


class CastDetail(DetailView):
    template_name = 'managerfilms/cast_detail.html'
    model = Cast
