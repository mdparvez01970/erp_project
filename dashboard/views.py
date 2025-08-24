from rest_framework import viewsets, permissions, filters
from .models import DashboardData
from .serializers import DashboardDataSerializer
from django_filters.rest_framework import DjangoFilterBackend

class DashboardDataViewSet(viewsets.ModelViewSet):
    queryset = DashboardData.objects.all()
    serializer_class = DashboardDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['id', 'value', 'last_updated']
    filterset_fields = ['name']
