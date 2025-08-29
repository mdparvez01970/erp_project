from django.urls import path
from .views import NotificationListAPIView, ReminderListAPIView

urlpatterns = [
    path("notifications/", NotificationListAPIView.as_view(), name="notification-list"),
    path("reminders/", ReminderListAPIView.as_view(), name="reminder-list"),
]
