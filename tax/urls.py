from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TaxRuleViewSet

router = DefaultRouter()
router.register(r'taxrules', TaxRuleViewSet)

urlpatterns = [path('', include(router.urls))]
