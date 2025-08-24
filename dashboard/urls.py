from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import DashboardDataViewSet

router = DefaultRouter()
router.register(r'dashboard', DashboardDataViewSet)

urlpatterns = [path('', include(router.urls))]
