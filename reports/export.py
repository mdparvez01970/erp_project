import io
import xlsxwriter
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def export_to_excel(queryset):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet('Reports')
    worksheet.write(0, 0, 'ID')
    worksheet.write(0, 1, 'Name')
    worksheet.write(0, 2, 'Generated At')
    for idx, report in enumerate(queryset, start=1):
        worksheet.write(idx, 0, report.id)
        worksheet.write(idx, 1, report.name)
        worksheet.write(idx, 2, report.generated_at.strftime("%Y-%m-%d %H:%M:%S"))
    workbook.close()
    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="reports.xlsx"'
    return response

def export_to_pdf(queryset):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    y = 800
    p.setFont("Helvetica-Bold", 14)
    p.drawString(200, y, "Reports List")
    y -= 40
    p.setFont("Helvetica", 12)
    for report in queryset:
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
