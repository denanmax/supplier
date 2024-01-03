from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter

from network.models import Manufacturer, Supplier, Product, Delivery
from network.paginators import ManufacturerPaginator
from network.permissions import IsActiveStuff
from network.serializers import ManufacturerSerializer, SupplierSerializer, ProductSerializer, DeliverySerializer


class SupplierViewSet(viewsets.ModelViewSet):
    """Вьюсет для Сапплаера с фильтрацией по стране"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveStuff]
    pagination_class = ManufacturerPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('country',)
    ordering_fields = ['country']


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveStuff]


class DeliveryAPIView(generics.ListAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsActiveStuff]


class ManufacturerAPIView(generics.ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    pagination_class = ManufacturerPaginator
    permission_classes = [IsActiveStuff]


class ManufacturerCreateAPIView(generics.CreateAPIView):
    serializer_class = ManufacturerSerializer
    permission_classes = [IsActiveStuff]


class ManufacturerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = [IsActiveStuff]


class ManufacturerUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = [IsActiveStuff]


class ManufacturerDestroyAPIView(generics.DestroyAPIView):
    queryset = Manufacturer.objects.all()
    permission_classes = [IsActiveStuff]
