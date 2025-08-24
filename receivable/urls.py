from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CustomerViewSet, SalesInvoiceViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'sales-invoices', SalesInvoiceViewSet)

urlpatterns = [path('', include(router.urls))]
