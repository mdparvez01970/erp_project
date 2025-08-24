from rest_framework import viewsets, permissions, filters
from .models import Asset
from .serializers import AssetSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'category']
    ordering_fields = ['purchase_date', 'purchase_value', 'current_value']
    filterset_fields = ['category', 'purchase_date']