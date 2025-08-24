from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BudgetViewSet

router = DefaultRouter()
router.register(r'budgets', BudgetViewSet)

urlpatterns = [path('', include(router.urls))]
