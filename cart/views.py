from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm



@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


@require_POST  # Ajout d'une vérification de méthode HTTP pour plus de sécurité
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
    coupon_apply_form = CouponApplyForm()
    return render(request, 'panier/panierdetail.html', {'cart': cart, 'coupon_apply_form': coupon_apply_form})


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')

from urllib.parse import quote


def redirect_to_whatsapp(request):
    cart = Cart(request)
    message = "Bonjour, je souhaite commander les produits suivants :\n"

    for item in cart:
        message += f"- {item['product'].name}, Quantité: {item['quantity']}\n"

    # Remplacez par le numéro de téléphone de l'entreprise
    phone_number = '22999954526'

    # Encoder le message pour qu'il soit compatible avec une URL
    url_encoded_message = quote(message)

    whatsapp_url = f"https://wa.me/{phone_number}?text={url_encoded_message}"

    return redirect(whatsapp_url)
