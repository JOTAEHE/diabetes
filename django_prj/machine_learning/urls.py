from django.urls import path
from . import views

# localhost : 8000 / blog

urlpatterns = [
    path('', views.index),
    path('result/', views.result),

]