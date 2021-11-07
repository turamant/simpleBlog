from django.urls import path

from apps.posts.views import list_post, detail_post, create_post, category, search

urlpatterns = [
    path('', list_post, name='list'),
    path('search/', search, name='search'),
    path('create/', create_post, name='create'),
    path('<slug:slug>/', detail_post, name='detail'),
    path('category/<slug:slug>/', category, name='category')

]