from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)
    exchange_rate = models.FloatField(default=1.0)

    def __str__(self):
        return self.code
