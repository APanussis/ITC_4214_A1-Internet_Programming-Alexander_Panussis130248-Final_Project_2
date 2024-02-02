from django.urls import path
from .views import viewProductInfo, viewProductCreate, viewProductSearch, viewTest

urlpatterns = [
    path('', viewProductSearch, name='home'),
    path('test/', viewTest, name='test'),
    path('productInfo/', viewProductInfo, name='productInfo'),
    path('productCreate/', viewProductCreate, name='productCreate'),
]