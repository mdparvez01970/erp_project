from rest_framework import status, viewsets, permissions, filters
from rest_framework.response import Response
from .models import Employee, Payslip
from .serializers import EmployeeSerializer, PayslipSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .utils import log_payslip_activity
from accounts.utils import log_activity

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['user__username', 'department']
    ordering_fields = ['id', 'joining_date', 'salary']
    
     # CREATE
    def perform_create(self, serializer):
        instance = serializer.save()
        log_activity(
            user=self.request.user,
            action="create",
            model_name=instance.__class__.__name__,
            object_id=instance.id,
            changes=str(serializer.validated_data)
        )
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        # UPDATE
    def perform_update(self, serializer):
        instance = serializer.save()
        log_activity(
            user=self.request.user,
            action="update",
            model_name=instance.__class__.__name__,
            object_id=instance.id,
            changes=str(serializer.validated_data)
        )

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        # DELETE
    def perform_destroy(self, instance):
        object_id = instance.id
        class_name = instance.__class__.__name__
        instance.delete()
        log_activity(
            user=self.request.user,
            action="delete",
            model_name=class_name,
            object_id=object_id,
            changes=None
        )

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PayslipViewSet(viewsets.ModelViewSet):
    queryset = Payslip.objects.all()
    serializer_class = PayslipSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['employee__user__username', 'month']
    ordering_fields = ['month', 'net_salary', 'basic']
    filterset_fields = ['employee', 'month']
    
    # CREATE
    def perform_create(self, serializer):
        instance = serializer.save()
        log_activity(
            user=self.request.user,
            action="create",
            model_name=instance.__class__.__name__,
            object_id=instance.id,
            changes=str(serializer.validated_data)
        )
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    
    # UPDATE
    def perform_update(self, serializer):
        instance = serializer.save()
        log_activity(
            user=self.request.user,
            action="update",
            model_name=instance.__class__.__name__,
            object_id=instance.id,
            changes=str(serializer.validated_data)
        )
    
    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    
    # DELETE
    def perform_destroy(self, instance):
        object_id = instance.id
        class_name = instance.__class__.__name__
        instance.delete()
        log_activity(
            user=self.request.user,
            action="delete",
            model_name=class_name,
            object_id=object_id,
            changes=None
        )
    
    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
