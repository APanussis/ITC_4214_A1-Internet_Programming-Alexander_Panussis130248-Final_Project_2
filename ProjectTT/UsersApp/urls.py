from django.urls import path, include
from .views import viewCustomLogin, viewCustomLogout, viewCustomSignup, viewProfile, viewProfileEdit

urlpatterns = [
    #path('', include("django.contrib.auth.urls")),
    
    path('login/', viewCustomLogin, name='login'),
    path('logout/', viewCustomLogout, name='logout'),
    path('signup/', viewCustomSignup, name='signup'),
    
    path('profile/', viewProfile, name='profile'),
    path('profileEdit/', viewProfileEdit, name='profileEdit'),
    # path('profileList/', viewProfileList, name='profileList'),
]