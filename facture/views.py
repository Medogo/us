from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Invoice
from django.shortcuts import redirect
from .models import Order
from .utils import generate_invoice_pdf, send_invoice_email



def invoice_detail(request, invoice_number):
    invoice = get_object_or_404(Invoice, invoice_number=invoice_number)
    return render(request, 'Invoices/facture.html', {'invoice': invoice})



def process_order(request):
    if request.method == 'POST':
        # Logique de traitement de la commande
        order = Order.objects.create(client=request.user)

        # Générer la facture PDF
        pdf_file = generate_invoice_pdf(order)

        # Envoyer l'email avec la facture
        send_invoice_email(order, pdf_file)

        return redirect('order_confirmation')