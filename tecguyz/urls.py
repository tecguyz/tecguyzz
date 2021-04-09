
from django.urls import path
# from django_filters.views import FilterView
from . import views
# from .filter import UserFilter, UserFilter2, UserFilter3
# from . views import ArticleDetail

urlpatterns=[
    path("", views.Homeview),
    path("Trending/<slug:slug>/", views.DetailViewTrending, name='detail_view_trending'),
    path("Latest/<slug:slug>/", views.DetailViewLatest, name='detail_view_latest'),
    path("Featured/<slug:slug>/", views.DetailViewFeatured, name='detail_view_featured'),
    path("Latest/", views.Latest, name='Latest'),
    path("Featured/", views.Featured, name='Featured'),
    path("Trending/", views.Trending, name='Trending')
    # path("searchbar/", views.searchbar, name='searchbar'),
    # path('search/',FilterView.as_view(filterset_class=UserFilter), name='search'),

    # path("Deals/<int:pk>/", views.DetailViewTrending, name='detail_view_deals'),
    # path('Trending/<int:pk>/',ArticleDetail.as_view(),name='detail_view'
]