from django.shortcuts import render
from rest_framework import generics, permissions
from .models import UploadedFile
from .serializers import UploadedFileSerializer

class FileUploadView(generics.ListCreateAPIView):
    serializer_class = UploadedFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UploadedFile.objects.filter(user=self.request.user).order_by('-uploaded_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
