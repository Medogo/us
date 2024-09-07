from django.urls import path
from .views import AuthView
app_name = 'accounts'
urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
]
