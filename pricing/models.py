from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    TYPE_CHOICES = [
        ('perishable', 'Perishable'),
        ('non-perishable', 'Non-Perishable'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.CharField(max_length=100)

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=100)
    base_distance_in_km = models.FloatField()
    km_price = models.DecimalField(max_digits=10, decimal_places=2)
    fix_price = models.DecimalField(max_digits=10, decimal_places=2)