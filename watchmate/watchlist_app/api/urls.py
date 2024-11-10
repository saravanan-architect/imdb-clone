from django.urls import path
from watchlist_app.api.views import MovieListAV, MovieDetailAV


urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('list/<int:pk>', MovieDetailAV.as_view(), name='movie-detail'),
]

# below code is for function based views
# from django.urls import path
# from watchlist_app.api.views import movie_list, movie_detail


# urlpatterns = [
#     path('list/', movie_list, name='movie-list'),
#     path('list/<int:pk>', movie_detail, name='movie-detail'),
# ]
