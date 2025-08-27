from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CurrencyViewSet, CurrencyRatesAPIView

router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet)

urlpatterns = [
    path('rates/', CurrencyRatesAPIView.as_view(), name='currency-rates'),
    
    path('', include(router.urls))
    ]
