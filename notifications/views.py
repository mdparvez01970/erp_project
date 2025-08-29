from django.shortcuts import render
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Notification, Reminder
from .serializers import NotificationSerializer, ReminderSerializer
from accounts.utils import log_activity

class NotificationListAPIView(generics.ListAPIView):
    queryset = Notification.objects.all().order_by("-created_at")
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['user__username', 'message', 'type']
    ordering_fields = ['created_at']
    filterset_fields = ['user', 'type', 'sent']

    def perform_create(self, serializer):
        instance = serializer.save()
        log_activity(
            user=self.request.user,
            action="create",
            model_name="Notification",
            object_id=instance.id,
            changes=str(serializer.validated_data)
        )

    def perform_update(self, serializer):
        instance = serializer.save()
        log_activity(
            user=self.request.user,
            action="update",
            model_name="Notification",
            object_id=instance.id,
            changes=str(serializer.validated_data)
        )

    def perform_destroy(self, instance):
        object_id = instance.id
        instance.delete()
        log_activity(
            user=self.request.user,
            action="delete",
            model_name="Notification",
            object_id=object_id,
            changes=None
        )

class ReminderListAPIView(generics.ListAPIView):
    queryset = Reminder.objects.all().order_by("due_date")
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['user__username', 'message', 'type']
    ordering_fields = ['due_date']
    filterset_fields = ['user', 'type', 'sent']

    def perform_create(self, serializer):
        instance = serializer.save()
        log_activity(
            user=self.request.user,
            action="create",
            model_name="Reminder",
            object_id=instance.id,
            changes=str(serializer.validated_data)
        )

    def perform_update(self, serializer):
        instance = serializer.save()
        log_activity(
            user=self.request.user,
            action="update",
            model_name="Reminder",
            object_id=instance.id,
            changes=str(serializer.validated_data)
        )

    def perform_destroy(self, instance):
        object_id = instance.id
        instance.delete()
        log_activity(
            user=self.request.user,
            action="delete",
            model_name="Reminder",
            object_id=object_id,
            changes=None
        )
