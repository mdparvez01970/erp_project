from django.db import models
from django.conf import settings
from accounts.models import User

class Income(models.Model):
    CATEGORY_CHOICES = (
        ('sales', 'Sales'),
        ('service', 'Service'),
        ('investment', 'Investment'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    source = models.CharField(max_length=100, default='Unknown')
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.amount}"
