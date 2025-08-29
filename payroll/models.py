from django.db import models
from django.conf import settings
from accounts.models import User
from django.utils import timezone
from cryptography.fernet import Fernet

f = Fernet(settings.FERNET_KEY)

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    joining_date = models.DateField(default=timezone.now)
    _salary  = models.BinaryField(null=True, blank=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
    @property
    def salary(self):
        if self._salary:
            return float(f.decrypt(self._salary).decode())
        return 0

    @salary.setter
    def salary(self, amount):
        self._salary = f.encrypt(str(amount).encode())

class Payslip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_index=True)
    month = models.DateField(db_index=True)
    basic = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    allowance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    net_salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    class Meta:
        indexes = [
            models.Index(fields=['employee', 'month']),
        ]
        
    def save(self, *args, **kwargs):
        self.net_salary = self.basic + self.allowance - self.deduction
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.user.username} - {self.month}"
