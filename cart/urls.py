from django.urls import path
from . import views
from .facture import generate_invoice

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('clear/', views.cart_clear, name='cart_clear'),  # Ajoutez cette ligne
    path('whatsapp/', views.redirect_to_whatsapp, name='redirect_to_whatsapp'),
    path('invoice/<int:order_id>/', generate_invoice, name='generate_invoice'),

]