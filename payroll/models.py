from django.db import models
from django.conf import settings
from accounts.models import User
from django.utils import timezone

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    joining_date = models.DateField(default=timezone.now)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Payslip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    basic = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    allowance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    net_salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.employee.user.username} - {self.month}"
