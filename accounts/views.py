from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, AccountHead, GeneralLedger
from .serializers import UserSerializer, AccountHeadSerializer, GeneralLedgerSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['username', 'email', 'role']
    ordering_fields = ['id', 'username', 'date_joined']
    filterset_fields = ['role', 'is_active']

class AccountHeadViewSet(viewsets.ModelViewSet):
    queryset = AccountHead.objects.all()
    serializer_class = AccountHeadSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'code']
    ordering_fields = ['id', 'code', 'name']
    filterset_fields = ['type']

class GeneralLedgerViewSet(viewsets.ModelViewSet):
    queryset = GeneralLedger.objects.all()
    serializer_class = GeneralLedgerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['description', 'account__name']
    ordering_fields = ['id', 'date', 'debit', 'credit']
    filterset_fields = ['date', 'account', 'account__type']
