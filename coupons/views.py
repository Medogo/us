from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponApplyForm


@require_POST
def coupon_apply(request):
    maintenant = timezone.now()
    formulaire = CouponApplyForm(request.POST)

    if formulaire.is_valid():
        code = formulaire.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(
                code__iexact=code,
                valid_from__lte=maintenant,
                valid_to__gte=maintenant,
                active=True
            )
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    else:
        request.session['coupon_id'] = None  # Réinitialiser le coupon si le formulaire est invalide

    return redirect('cart:cart_detail')
