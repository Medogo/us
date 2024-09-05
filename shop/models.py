from datetime import timezone
#from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_vedette = models.BooleanField(default=False)
    #is_promo = models.BooleanField(default=False)
    is_discover = models.BooleanField(default=False)
    is_plus_vendus = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['id', 'slug']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class SliderProduit(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name


class PromotionProduit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_promotion = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()
    messages = models.TextField()
    expiration = models.BooleanField(default=False)

    def expired(self):
        """
        Cette méthode vérifie si la promotion est expirée en comparant la date actuelle
        avec la date d'expiration de la promotion.
        """
        if timezone.now() > self.expire_date:
            self.expiration = True
            self.save()
        return self.expiration
