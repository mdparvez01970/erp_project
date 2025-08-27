from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=5, unique=True, db_index=True)
    name = models.CharField(max_length=50, db_index=True)
    exchange_rate = models.FloatField(default=1.0)

    def __str__(self):
        return self.code
