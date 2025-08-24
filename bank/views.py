from rest_framework import viewsets, permissions, filters
from .models import BankAccount, Transaction
from .serializers import BankAccountSerializer, TransactionSerializer
from django_filters.rest_framework import DjangoFilterBackend

class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'account_number']
    ordering_fields = ['balance']
    filterset_fields = ['account_number']

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['description']
    ordering_fields = ['amount', 'date']
    filterset_fields = ['bank_account', 'type', 'date']
