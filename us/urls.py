from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    #re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path("__reload__/", include("django_browser_reload.urls")),

    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),

    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),

    path('coupons/', include('coupons.urls', namespace='coupons')),

    path('facture/', include('facture.urls', namespace='facture')),
    path('', include('shop.urls', namespace='home')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
