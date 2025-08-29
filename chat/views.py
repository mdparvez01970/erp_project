from django.shortcuts import render
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Message
from .serializers import MessageSerializer
from accounts.utils import log_activity

class MessageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['sender__username', 'receiver__username', 'content']
    ordering_fields = ['sent_at']
    filterset_fields = ['sender', 'receiver']

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(sender=user) | Message.objects.filter(receiver=user)


    def perform_create(self, serializer):
        instance = serializer.save()
        log_activity(
            user=self.request.user,
            action="create",
            model_name="Message",
            object_id=instance.id,
            changes=str(serializer.validated_data)
        )

    def perform_update(self, serializer):
        instance = serializer.save()
        log_activity(
            user=self.request.user,
            action="update",
            model_name="Message",
            object_id=instance.id,
            changes=str(serializer.validated_data)
        )

    def perform_destroy(self, instance):
        object_id = instance.id
        instance.delete()
        log_activity(
            user=self.request.user,
            action="delete",
            model_name="Message",
            object_id=object_id,
            changes=None
        )