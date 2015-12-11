from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import MovieList, CastList, GenreDetail, MovieDetail, CastDetail

urlpatterns = patterns(
    'managerfilms.views',
    url(r'^movie/$', MovieList.as_view(), name='movie_list'),
    url(r'^movie/(?P<pk>\d+)/$',
        MovieDetail.as_view(), name='movie_detail'),

    url(r'^cast/$', CastList.as_view(), name='cast_list'),
    url(r'^cast/(?P<pk>\d+)/$',
        CastDetail.as_view(), name='cast_detail'),

    url(r'^genre/$', GenreDetail.as_view(), name='genre_list'),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
