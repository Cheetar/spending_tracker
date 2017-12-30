from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('board/(?P<id>\d+)/', views.board, name='board'),
]
