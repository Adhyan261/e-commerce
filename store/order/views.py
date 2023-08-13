from django.shortcuts import get_object_or_404
from rest_framework import viewsets,generics
from order.models import Order, OrderItem
from order.serializers import OrderItemSerializer, OrderReadSerializer, OrderWriteSerializer


class OrderItemViewSet(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderViewSet(generics.ListCreateAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderWriteSerializer

        return OrderReadSerializer


