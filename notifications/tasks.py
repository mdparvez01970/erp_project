from celery import shared_task
from django.utils import timezone
from .models import Reminder, Notification

@shared_task
def send_reminders():
    reminders = Reminder.objects.filter(sent=False, due_date__lte=timezone.now())
    for r in reminders:
        # Example: create Notification (simulate sending email/SMS/push)
        Notification.objects.create(user=r.user, message=r.message, type="email")
        r.sent = True
        r.save()
