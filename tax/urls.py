from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TaxRuleViewSet, TaxConfigAPIView

router = DefaultRouter()
router.register(r'taxrules', TaxRuleViewSet)

urlpatterns = [
    path('config/', TaxConfigAPIView.as_view(), name='tax-config'),
    
    path('', include(router.urls))
    ]
