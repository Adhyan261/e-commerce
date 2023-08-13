from django.urls import path,include
from .views import OrderItemViewSet,OrderViewSet
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('orders/', OrderViewSet.as_view(),),
    path('orders/<int:pk>/', OrderItemViewSet.as_view(), ),
]