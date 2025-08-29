from django.shortcuts import render
from rest_framework import generics, permissions
from .models import ActivityLog
from .serializers import ActivityLogSerializer

class ActivityLogListAPIView(generics.ListAPIView):
    queryset = ActivityLog.objects.all().order_by('-timestamp')
    serializer_class = ActivityLogSerializer
    permission_classes = [permissions.IsAuthenticated]
