from django.urls import path
from .views import viewProductInfo, viewProductCreate, viewProductSearch, viewProductEdit, viewProductDelete, viewTest


urlpatterns = [
    path('test/', viewTest, name='test'),
    path('home/', viewProductSearch, name='home'),
    path('productCreate/', viewProductCreate, name='productCreate'),
    path('<int:id>/productInfo/', viewProductInfo, name='productInfo'),
    path('<int:id>/productEdit/', viewProductEdit, name='productEdit'),
    path('<int:id>/productDelete/', viewProductDelete, name='productDelete'),
]