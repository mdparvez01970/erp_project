from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Workflow, Approval
from .serializers import WorkflowSerializer, ApprovalSerializer

class WorkflowViewSet(viewsets.ModelViewSet):
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer
    permission_classes = [permissions.IsAuthenticated]

class ApprovalViewSet(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        approval = self.get_object()
        status_value = request.data.get('status')
        comments = request.data.get('comments', '')
        if status_value not in [a[0] for a in approval._meta.get_field('status').choices]:
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)
        approval.status = status_value
        approval.comments = comments
        approval.save()
        return Response(self.get_serializer(approval).data)

