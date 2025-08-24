from django.db import models
from django.conf import settings

class DashboardData(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
