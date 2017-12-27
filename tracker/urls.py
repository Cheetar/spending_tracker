from django.urls import include, path

from . import registration_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', registration_views.profile, name='profile'),
    path('accounts/register/', registration_views.register, name='register'),
]
