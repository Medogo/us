# Generated by Django 5.1 on 2024-09-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0004_alter_invoice_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(default='BCB84E11214A', editable=False, max_length=12, unique=True),
        ),
    ]
