from rest_framework import status, viewsets, permissions, filters
from rest_framework.views import APIView
from .models import Currency
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CurrencySerializer
from .utils import get_currency_rates
from django_filters.rest_framework import DjangoFilterBackend

class CurrencyRatesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rates = get_currency_rates()
        return Response(rates)

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['code', 'name']
    ordering_fields = ['id', 'code', 'exchange_rate']
    filterset_fields = ['code']
    
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({
                "success": False,
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response({
                "success": False,
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

