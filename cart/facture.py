# facture.py
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa
from contact.models import Company
from order.models import Order


def render_to_pdf(template_src, context_dict):
    template = render_to_string(template_src, context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(template.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None

def generate_invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    company = get_object_or_404(Company, id=1)  # Assuming you have only one company record for simplicity
    context = {'order': order, 'company': company}
    pdf_content = render_to_pdf('Invoices/facture.html', context)

    if pdf_content:
        response = HttpResponse(pdf_content, content_type='application/pdf')
        filename = f"Invoice_{order.order_number}.pdf"
        content = f"attachment; filename={filename}"
        response['Content-Disposition'] = content
        return response

    return HttpResponse("Error generating PDF", status=500)
