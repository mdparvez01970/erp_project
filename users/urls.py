from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AuditLogViewSet

router = DefaultRouter()
router.register(r'audit-logs', AuditLogViewSet)

urlpatterns = [path('', include(router.urls))]
