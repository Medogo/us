from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'customer', 'address', 'postal_code', 'city', 'created', 'updated', 'paid']
    list_filter = ['paid', 'created', 'updated', 'city']
    search_fields = ['order_number', 'customer__username', 'customer__email']
    inlines = [OrderItemInline]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity', 'get_cost']
    search_fields = ['order__order_number', 'product__name']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
