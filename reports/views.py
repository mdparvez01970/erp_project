from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Report
from .serializers import ReportSerializer
import io
import xlsxwriter
from reportlab.pdfgen import canvas
from django_filters.rest_framework import DjangoFilterBackend

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['id', 'generated_at']
    filterset_fields = ['generated_at']
    
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

    @action(detail=False, methods=['get'])
    def export_excel(self, request):
        try:
            output = io.BytesIO()
            workbook = xlsxwriter.Workbook(output)
            worksheet = workbook.add_worksheet('Reports')
            worksheet.write(0, 0, 'ID')
            worksheet.write(0, 1, 'Name')
            worksheet.write(0, 2, 'Generated At')
            for idx, report in enumerate(self.get_queryset(), start=1):
                worksheet.write(idx, 0, report.id)
                worksheet.write(idx, 1, report.name)
                worksheet.write(idx, 2, report.generated_at.strftime("%Y-%m-%d %H:%M:%S"))
            workbook.close()
            output.seek(0)
            response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="reports.xlsx"'
            return response
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def export_pdf(self, request):
        try:
            buffer = io.BytesIO()
            p = canvas.Canvas(buffer)
            y = 800
            p.setFont("Helvetica-Bold", 14)
            p.drawString(200, y, "Reports List")
            y -= 40
            p.setFont("Helvetica", 12)
            for report in self.get_queryset():
                p.drawString(50, y, f"ID: {report.id}  Name: {report.name}  Generated At: {report.generated_at.strftime('%Y-%m-%d %H:%M:%S')}")
                y -= 20
                if y < 50:
                    p.showPage()
                    y = 800
            p.save()
            buffer.seek(0)
            response = HttpResponse(buffer, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reports.pdf"'
            return response
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
