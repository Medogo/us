from django.contrib import admin
from .models import Category, Product


#register
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


from .models import PromotionProduit


class PromotionProduitAdmin(admin.ModelAdmin):
    list_display = ('product', 'date_promotion', 'expire_date', 'expiration')  # Les champs à afficher dans la liste
    list_filter = ('product', 'expire_date', 'expiration')  # Filtres disponibles
    search_fields = (
    'product__name',)  # Permet de rechercher un produit par nom (si le champ "name" existe dans le modèle Product)
    date_hierarchy = 'date_promotion'  # Ajoute une hiérarchie des dates pour "date_promotion"


admin.site.register(PromotionProduit, PromotionProduitAdmin)
