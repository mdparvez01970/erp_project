from rest_framework import viewsets, filters
from .models import Expense
from .serializers import ExpenseSerializer
from accounts.permission import IsManagerOrAdmin
from django_filters.rest_framework import DjangoFilterBackend

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsManagerOrAdmin]  # Only admin/manager can access
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['description', 'category', 'user__username']
    ordering_fields = ['id', 'amount', 'date']
    filterset_fields = ['category', 'date', 'user']

