from django.contrib import admin
from django.urls import path

from .views import ProductViewSet, OfferViewSet

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get':'get',
        'post': 'create'
        })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
        })),
    path('offers', OfferViewSet.as_view({
        'get':'get',
        'post': 'create'
        })),
    path('offers/<str:pk>', OfferViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
        })),
  
]
