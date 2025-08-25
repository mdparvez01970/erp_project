from django.db import models
from django.conf import settings
from datetime import date

class Asset(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    purchase_date = models.DateField()
    purchase_value = models.DecimalField(max_digits=12, decimal_places=2)
    depreciation_rate = models.FloatField(default=0)
    current_value = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name
