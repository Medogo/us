from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code

    def clean(self):
        # Vérification que valid_to est postérieur à valid_from
        if self.valid_to <= self.valid_from:
            raise ValidationError("La date de fin de validité doit être postérieure à la date de début.")

    def calculate_discount(self, total_amount):
        """
        Calcule le montant de la réduction sur un total donné.
        """
        return (self.discount / 100) * total_amount

    def save(self, *args, **kwargs):
        # Désactiver automatiquement le coupon si les dates ne sont pas valides
        if self.valid_to <= self.valid_from:
            self.active = False
        super().save(*args, **kwargs)
