from django.contrib import admin
from .models import MessagesList, Contact

@admin.register(MessagesList)
class MessagesListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'date', 'date_update')
    list_filter = ('date', 'date_update')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('date', 'date_update')
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('Dates', {
            'fields': ('date', 'date_update'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'telephone', 'location')
    search_fields = ('address', 'telephone', 'location')