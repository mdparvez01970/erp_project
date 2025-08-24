from django.db import models
from django.conf import settings
from accounts.models import User

class Expense(models.Model):
    CATEGORY_CHOICES = (
        ('office', 'Office'),
        ('travel', 'Travel'),
        ('utilities', 'Utilities'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()
    receipt = models.FileField(upload_to='receipts/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.amount}"
