from django.urls import path, include
from .views import viewProfile, viewProfileList

urlpatterns = [
    #path('login/', viewLogin, name='login'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('profile/', viewProfile, name='profile'),
    path('profileList/', viewProfileList, name='profileList'),
]