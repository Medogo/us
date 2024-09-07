from django.urls import path
from . import views


app_name = 'contact'
urlpatterns = [
    path('', views.message, name='contact'),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
