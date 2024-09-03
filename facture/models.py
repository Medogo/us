from django.db import models
import uuid
from django.db import models
from django.utils import timezone
from order.models import Order

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=12, unique=True, editable=False, default=uuid.uuid4().hex[:12].upper())
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='invoice')
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    payment_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Invoice {self.invoice_number} for Order {self.order.order_number}'

    def get_total_amount(self):
        return self.order.get_total_cost()

    def is_overdue(self):
        if self.due_date and not self.paid:
            return self.due_date < timezone.now().date()
        return False
