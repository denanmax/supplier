import django_filters
from rest_framework import generics, viewsets
from network.models import Manufacturer, Supplier, Product, Delivery
from network.permissions import IsActiveStuff
from network.serializers import ManufacturerSerializer, SupplierSerializer, ProductSerializer, DeliverySerializer


class ManufacturerAPIView(generics.ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
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


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveStuff]


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveStuff]


class DeliveryViewSet(viewsets.ModelViewSet):
    serializer_class = DeliverySerializer
    queryset = Delivery.objects.all()
    permission_classes = [IsActiveStuff]
