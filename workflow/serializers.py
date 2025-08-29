from rest_framework import serializers
from .models import Workflow, Approval

class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approval
        fields = ['id', 'workflow', 'level', 'user', 'status', 'comments', 'updated_at']

class WorkflowSerializer(serializers.ModelSerializer):
    approvals = ApprovalSerializer(many=True, read_only=True)
    class Meta:
        model = Workflow
        fields = ['id', 'module_name', 'description', 'approvals', 'created_at']
