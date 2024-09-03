from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderCreateForm
import logging

logger = logging.getLogger(__name__)

@login_required
def order_create(request):
    cart = Cart(request)
    if not cart:
        return redirect('cart:cart_detail')  # Rediriger si le panier est vide

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    order = form.save(commit=False)
                    order.customer = request.user
                    order.save()
                    total_cost = 0
                    for item in cart:
                        OrderItem.objects.create(
                            order=order,
                            product=item['product'],
                            price=item['price'],
                            quantity=item['quantity']
                        )
                        total_cost += item['price'] * item['quantity']
                    order.total = total_cost
                    order.save()
                    cart.clear()
                return render(request, 'order/created.html', {'order': order})
            except Exception as e:
                logger.error(f"Erreur lors de la création de la commande: {str(e)}")
                form.add_error(None, "Une erreur est survenue lors de la création de la commande.")
    else:
        form = OrderCreateForm(initial={'customer': request.user})

    return render(request, 'order/create.html', {'cart': cart, 'form': form})