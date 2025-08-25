from rest_framework import status, viewsets, permissions, filters
from rest_framework.response import Response
from .models import Supplier, PurchaseInvoice
from .serializers import SupplierSerializer, PurchaseInvoiceSerializer
from rest_framework.decorators import action
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import PurchaseInvoice
import io
from django_filters.rest_framework import DjangoFilterBackend

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'email', 'phone']
    ordering_fields = ['id', 'name']
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PurchaseInvoiceViewSet(viewsets.ModelViewSet):
    queryset = PurchaseInvoice.objects.all()
    serializer_class = PurchaseInvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['invoice_number', 'supplier__name']
    ordering_fields = ['id', 'amount', 'due_date']
    filterset_fields = ['paid', 'supplier']
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def generate_invoice(self, request, pk=None):
        try:
            invoice = self.get_object()
            buffer = io.BytesIO()
            p = canvas.Canvas(buffer)
            # Logo
            try:
                p.drawImage("static/logo.png", 50, 750, width=100, height=50)
            except Exception:
                pass  # Ignore if logo missing
            # Invoice details
            p.setFont("Helvetica-Bold", 16)
            p.drawString(200, 780, f"Invoice: {invoice.invoice_number}")
            p.setFont("Helvetica", 12)
            p.drawString(50, 720, f"Supplier: {invoice.supplier.name}")
            p.drawString(50, 700, f"Amount: {invoice.amount}")
            p.drawString(50, 680, f"Due Date: {invoice.due_date}")
            p.save()
            buffer.seek(0)
            return HttpResponse(buffer, content_type='application/pdf')
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
