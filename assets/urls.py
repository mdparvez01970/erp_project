from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AssetViewSet

router = DefaultRouter()
router.register(r'assets', AssetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
