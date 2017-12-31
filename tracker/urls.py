from django.urls import include, path

from . import registration_views, views

handler404 = 'tracker.views.handler404'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/profile/', registration_views.profile, name='profile'),
    path('accounts/register/', registration_views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
