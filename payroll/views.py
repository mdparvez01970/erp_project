from rest_framework import viewsets, permissions, filters
from .models import Employee, Payslip
from .serializers import EmployeeSerializer, PayslipSerializer
from django_filters.rest_framework import DjangoFilterBackend

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['user__username', 'department']
    ordering_fields = ['id', 'joining_date', 'salary']

class PayslipViewSet(viewsets.ModelViewSet):
    queryset = Payslip.objects.all()
    serializer_class = PayslipSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['employee__user__username', 'month']
    ordering_fields = ['month', 'net_salary', 'basic']
    filterset_fields = ['employee', 'month']
