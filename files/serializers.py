from rest_framework import serializers
from .models import UploadedFile

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'user', 'file', 'description', 'uploaded_at']
        read_only_fields = ['user', 'uploaded_at']

    def validate_file(self, value):
        import os
        ext = os.path.splitext(value.name)[1].lower()
        allowed_extensions = ['.pdf', '.jpg', '.jpeg', '.png', '.docx', '.xlsx']
        if ext not in allowed_extensions:
            raise serializers.ValidationError("Unsupported file extension.")
        if value.size > 10*1024*1024:
            raise serializers.ValidationError("File too large. Max size is 10MB.")
        return value
