from rest_framework import viewsets, permissions, filters
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['sku', 'name', 'category', 'supplier']
    ordering_fields = ['id', 'stock', 'price', 'name']
    filterset_fields = ['category', 'supplier']
