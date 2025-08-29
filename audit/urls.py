from django.urls import path
from .views import ActivityLogListAPIView

urlpatterns = [
    path('logs/', ActivityLogListAPIView.as_view(), name='activity-log-list'),
]
