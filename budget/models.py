from django.db import models
from django.conf import settings
from django.utils import timezone

class Budget(models.Model):
    name = models.CharField(max_length=100, default='Unnamed Budget')
    department = models.CharField(max_length=100)
    allocated_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    spent_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.name} - {self.department}"
