from django.urls import path
from .views import viewProductInfo, viewProductCreate, viewProductSearch, cViewProductSearchResults

urlpatterns = [
    path('test/', viewProductSearch, name='test'),
    path('results/', cViewProductSearchResults.as_view(), name='productSearchResults'),
    path('productInfo/', viewProductInfo, name='productInfo'),
    path('productCreate/', viewProductCreate, name='productCreate'),
]