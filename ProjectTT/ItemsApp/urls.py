from django.urls import path
from .views import viewProductInfo, viewProductCreate, viewProductSearch

urlpatterns = [
    path('test/', viewProductSearch, name='test'),
    path('productInfo/', viewProductInfo, name='productInfo'),
    path('productCreate/', viewProductCreate, name='productCreate'),
]