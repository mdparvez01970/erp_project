from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff', db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    username = models.CharField(max_length=150, unique=True, db_index=True)
    
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
    name = models.CharField(max_length=100, db_index=True)
    code = models.CharField(max_length=20, unique=True, db_index=True)
    type = models.CharField(max_length=20, choices=ACCOUNT_TYPES,default='ASSET', db_index=True)
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class GeneralLedger(models.Model):
    date = models.DateField(db_index=True)
    account = models.ForeignKey(AccountHead, on_delete=models.CASCADE, db_index=True)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['account', 'date']),
        ]
    
    def __str__(self):
        return f"{self.date} | {self.account.name} | D:{self.debit} C:{self.credit}"
