from rest_framework import viewsets, permissions, filters
from .models import AuditLog
from .serializers import AuditLogSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['user__username', 'action']
    ordering_fields = ['id', 'timestamp']
    filterset_fields = ['user']
