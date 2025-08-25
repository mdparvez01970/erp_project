from rest_framework import serializers
from .models import AuditLog

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'
        
    def validate_action(self, value):
        if not value.strip():
            raise serializers.ValidationError("Action field cannot be empty.")
        return value
