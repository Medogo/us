from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch


def generate_invoice_pdf(order):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # En-tête
    p.setFont("Helvetica-Bold", 16)
    p.drawString(1 * inch, 10 * inch, "Facture")
    p.setFont("Helvetica", 12)
    p.drawString(1 * inch, 9.5 * inch, f"Numéro de commande: {order.id}")
    p.drawString(1 * inch, 9 * inch, f"Date: {order.date_created.strftime('%d/%m/%Y')}")

    # Informations client
    p.drawString(1 * inch, 8 * inch, f"Client: {order.client.nom} {order.client.prenom}")
    p.drawString(1 * inch, 7.5 * inch, f"Email: {order.client.email}")

    # Détails de la commande
    p.drawString(1 * inch, 6.5 * inch, "Détails de la commande:")
    y = 6 * inch
    for item in order.items.all():
        p.drawString(1 * inch, y, f"{item.product.name} - Quantité: {item.quantity} - Prix: {item.price}€")
        y -= 0.5 * inch

    # Total
    p.drawString(1 * inch, y - 0.5 * inch, f"Total: {order.total_price}€")

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer


from django.core.mail import EmailMessage

def send_invoice_email(order, pdf_file):
    subject = f"Facture pour votre commande #{order.id}"
    body = f"""
    Cher/Chère {order.client.nom} {order.client.prenom},

    Merci pour votre achat. Veuillez trouver ci-joint la facture pour votre commande #{order.id}.

    Cordialement,
    Votre équipe
    """
    email = EmailMessage(
        subject,
        body,
        'votre_email@example.com',
        [order.client.email],
    )
    email.attach(f'facture_{order.id}.pdf', pdf_file.getvalue(), 'application/pdf')
    email.send()