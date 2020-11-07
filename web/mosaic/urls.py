from django.urls import path

from . import views

app_name = 'mosaic'
urlpatterns = [
    path('', views.index, name='index'),
    path('draw/', views.draw, name='draw')
]