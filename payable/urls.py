from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import SupplierViewSet, PurchaseInvoiceViewSet

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'purchase-invoices', PurchaseInvoiceViewSet)

urlpatterns = [path('', include(router.urls))]
