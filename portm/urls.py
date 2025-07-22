from django.urls import path
from . import views

urlpatterns = [
  #  path('publications/', views.publication_list, name='publication_list'),
    path('', views.index, name='index'),
    
]




