from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('paper/', views.index_paper, name='index_paper'),
]
