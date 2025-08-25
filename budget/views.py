from rest_framework import status, viewsets, permissions, filters
from .models import Budget
from .serializers import BudgetSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'department']
    ordering_fields = ['allocated_amount', 'spent_amount', 'start_date', 'end_date']
    filterset_fields = ['department', 'start_date', 'end_date']
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({
                "success": False,
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
