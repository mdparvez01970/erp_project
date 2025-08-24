from rest_framework import viewsets, permissions, filters
from .models import Budget
from .serializers import BudgetSerializer
from django_filters.rest_framework import DjangoFilterBackend

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'department']
    ordering_fields = ['allocated_amount', 'spent_amount', 'start_date', 'end_date']
    filterset_fields = ['department', 'start_date', 'end_date']
