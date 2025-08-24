from rest_framework import viewsets, permissions, filters
from .models import TaxRule
from .serializers import TaxRuleSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TaxRuleViewSet(viewsets.ModelViewSet):
    queryset = TaxRule.objects.all()
    serializer_class = TaxRuleSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'type']
    ordering_fields = ['id', 'rate']
    filterset_fields = ['type']
    
    
