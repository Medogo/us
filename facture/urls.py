from django.urls import path
from . import views

app_name = 'invoices'

urlpatterns = [
    path('invoice/<str:invoice_number>/', views.invoice_detail, name='invoice_detail'),
]
