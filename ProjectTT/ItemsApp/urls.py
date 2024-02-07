from django.urls import path
from .views import viewProductInfo, viewProductCreate, viewProductSearch, viewProductEdit, viewTest

urlpatterns = [
    path('test/', viewTest, name='test'),
    path('home/', viewProductSearch, name='home'),
    path('productCreate/', viewProductCreate, name='productCreate'),
    path('productInfo/<int:id>/', viewProductInfo, name='productInfo'),
    path('productEdit/<int:id>/', viewProductEdit, name='productEdit'),
]