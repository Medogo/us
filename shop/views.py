from django.shortcuts import render, get_object_or_404
from .models import Category, Product, PromotionProduit
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    product_promo = PromotionProduit.objects.all().first()
    products_is_vedettes = Product.objects.filter(is_vedette=True)
    products_plus_vendus = Product.objects.filter(is_plus_vendus=True).all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'product_promo': product_promo,
        'products_plus_vendus': products_plus_vendus,
        'products_is_vedettes': products_is_vedettes
    }
    return render(request, 'shop/index.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/detailproduit.html', context)

