from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.showview, name='dashboard'),
    path('show/', views.showview, name='dashboard'),
    path('post/', views.NewsCreateView.as_view(), name='news-create'),
    path('show/vote/<int:pk>/<str:up_or_down>/', views.vote, name='book-vote'),
    path('show/<int:pk>/', views.comment_news, name='show-comments'),
    path('kinderübersicht/', include('kinderübersicht.urls')),
]
