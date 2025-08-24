from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')
    
    def __str__(self):
        return self.username

class AccountHead(models.Model):
    ACCOUNT_TYPES = [
        ('ASSET', 'Asset'),
        ('LIABILITY', 'Liability'),
        ('EQUITY', 'Equity'),
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense')
    ]
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20, choices=ACCOUNT_TYPES,default='ASSET')
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class GeneralLedger(models.Model):
    date = models.DateField()
    account = models.ForeignKey(AccountHead, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.date} | {self.account.name} | D:{self.debit} C:{self.credit}"
