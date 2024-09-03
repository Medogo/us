from django.contrib import admin
from .models import Message, Contact

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'content')  # Colonnes affichées
    search_fields = ('name', 'email')  # Champs de recherche
    list_filter = ('email',)  # Filtres disponibles
    ordering = ('name',)  # Ordre par défaut
    fields = ('name', 'email', 'content', 'messages')  # Champs à afficher dans le formulaire d'ajout/modification

class ContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'telephone', 'location')  # Colonnes affichées
    search_fields = ('address', 'telephone')  # Champs de recherche
    ordering = ('address',)  # Ordre par défaut
    fields = ('address', 'telephone', 'location')  # Champs à afficher dans le formulaire d'ajout/modification

# Enregistrez vos modèles avec leur configuration dans l'admin
admin.site.register(Message, MessageAdmin)
admin.site.register(Contact, ContactAdmin)
