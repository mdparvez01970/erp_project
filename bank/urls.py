from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BankAccountViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'bankaccounts', BankAccountViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
