from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import IncomeViewSet

router = DefaultRouter()
router.register(r'incomes', IncomeViewSet)

urlpatterns = [path('', include(router.urls))]
