from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        
    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Report name must be at least 2 characters long.")
        return value

    def validate_file(self, value):
        if not value:
            raise serializers.ValidationError("File is required.")
        return value
