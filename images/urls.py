from django.urls import path, re_path
from . import views

app_name = 'images'

urlpatterns = [
    # path('create/', views.image_create, name='create'),
    path('create/', views.ImageCreateView.as_view(), name='create'),
    # path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
    # path('detail/<int:id>/<slug:slug>/', views.ImageDetailView.as_view(), name='detail'),
    re_path(r'^(?P<id>[0-9]{1,})/(?P<slug>[-\w]+)/$', views.ImageDetailView.as_view(), name='detail'),
    # path('like/', views.image_like, name='like'),
    path('like/', views.ImageLikeView.as_view(), name='like'),
    # path('', views.image_list, name='list'),
    path('', views.ImageListView.as_view(), name='list'),
    # path('ranking/', views.image_ranking, name='ranking'),
    path('ranking/', views.ImageRankingView.as_view(), name='ranking'),
]