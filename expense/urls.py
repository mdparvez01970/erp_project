from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ExpenseViewSet

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [path('', include(router.urls))]
