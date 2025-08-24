from rest_framework import viewsets, permissions, filters
from .models import Currency
from .serializers import CurrencySerializer
from django_filters.rest_framework import DjangoFilterBackend

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['code', 'name']
    ordering_fields = ['id', 'code', 'exchange_rate']
    filterset_fields = ['code']

