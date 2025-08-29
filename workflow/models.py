from django.db import models
from django.conf import settings
from django.utils import timezone

class ApprovalLevel(models.TextChoices):
    MANAGER = "manager", "Manager"
    ADMIN = "admin", "Admin"
    FINANCE = "finance", "Finance"

class ApprovalStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    APPROVED = "approved", "Approved"
    REJECTED = "rejected", "Rejected"

class Workflow(models.Model):
    module_name = models.CharField(max_length=50)  # e.g., Expense, Leave, Invoice
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.module_name

class Approval(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='approvals')
    level = models.CharField(max_length=20, choices=ApprovalLevel.choices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=ApprovalStatus.choices, default=ApprovalStatus.PENDING)
    comments = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('workflow', 'level')  # Each level appears once per workflow

    def __str__(self):
        return f"{self.workflow.module_name} - {self.level} - {self.status}"
