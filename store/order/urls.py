from django.urls import path,include
from .views import OrderViewSet,OrderUpdate
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('orders/', OrderViewSet.as_view(),),
   path('orders/<int:pk>/', OrderUpdate.as_view(), ),
]