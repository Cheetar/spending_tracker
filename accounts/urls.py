from django.urls import include, path

from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
