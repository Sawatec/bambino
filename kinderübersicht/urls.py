from django.urls import path

from . import views

urlpatterns = [
    path('showKinder/', views.showChildrenView, name='kinderübersicht'),
    path('showKinder/<int:pk>/', views.showInfoChild, name='show-info'),
]