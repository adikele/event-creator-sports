from django.urls import path
from . import views

#adding 8.7 in Czech Labhna

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.EventListView.as_view(), name='events'),
]

#adding 13.7 in Oodi