from rest_framework import viewsets, permissions, filters
from .models import Customer, SalesInvoice
from .serializers import CustomerSerializer, SalesInvoiceSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'email', 'phone']
    ordering_fields = ['id', 'name']

class SalesInvoiceViewSet(viewsets.ModelViewSet):
    queryset = SalesInvoice.objects.all()
    serializer_class = SalesInvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['invoice_number', 'customer__name']
    ordering_fields = ['id', 'amount', 'due_date']
    filterset_fields = ['customer', 'paid', 'due_date']
