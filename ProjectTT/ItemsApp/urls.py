from django.urls import path
from .views import viewTest, viewProductSearch, viewOptionsCreate, viewProductCreate, viewProductInfo, viewProductEdit ,viewProductDelete

urlpatterns = [
    path('test/', viewTest, name='test'),
    path('home/', viewProductSearch, name='home'),
    path('optionsCreate/', viewOptionsCreate, name='optionsCreate'),
    path('productCreate/', viewProductCreate, name='productCreate'),
    path('<int:id>/productInfo/', viewProductInfo, name='productInfo'),
    path('<int:id>/productEdit/', viewProductEdit, name='productEdit'),
    path('<int:id>/productDelete/', viewProductDelete, name='productDelete'),
]