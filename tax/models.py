from django.db import models
from django.conf import settings

class TaxRule(models.Model):
    name = models.CharField(max_length=100)
    rate = models.FloatField()
    type = models.CharField(max_length=50, choices=(('VAT','VAT'),('GST','GST'),('Income','Income')))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.name} - {self.type}"
