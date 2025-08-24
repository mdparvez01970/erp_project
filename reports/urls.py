from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ReportViewSet

router = DefaultRouter()
router.register(r'reports', ReportViewSet)

urlpatterns = [path('', include(router.urls))]
