from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('create_user/', views.CreateUser.as_view(), name='create_user'),
    path('warning/', TemplateView.as_view(template_name='createWarning.html'), name='warning'),
]