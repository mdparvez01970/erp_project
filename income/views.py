from rest_framework import viewsets, permissions, filters
from .models import Income
from .serializers import IncomeSerializer
from django_filters.rest_framework import DjangoFilterBackend

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['source', 'description', 'category', 'user__username']
    ordering_fields = ['id', 'amount', 'date']
    filterset_fields = ['category', 'date', 'user']

