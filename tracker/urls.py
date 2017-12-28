from django.urls import include, path

from . import registration_views, views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', registration_views.profile, name='profile'),
    path('accounts/register/', registration_views.register, name='register'),
]
