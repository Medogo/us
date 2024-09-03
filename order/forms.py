from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    agree_to_terms = forms.BooleanField(
        required=True,
        label="J'accepte les conditions d'utilisation"
    )

    class Meta:
        model = Order
        fields = ['customer', 'address', 'postal_code', 'city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    # Supprimez la méthode clean_email car le champ email n'est pas dans le modèle Order