from django.urls import path

from . import views

handler404 = 'tracker.views.handler404'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('board/<int:id>/', views.board, name='board'),
    path('board/export/<int:id>/', views.export, name='export'),
    path('board/analytics/<int:id>/', views.analytics, name='analytics'),
    path('board/settings/<int:id>/', views.board_settings, name='board_settings'),
    path('board/create/', views.create_board, name='create_board'),
]
