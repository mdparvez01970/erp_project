from django.db import models
from django.conf import settings

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, choices=[("email","Email"),("sms","SMS"),("push","Push")])

    def __str__(self):
        return f"{self.user.username} - {self.type}"
    

class Reminder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    due_date = models.DateTimeField()
    type = models.CharField(max_length=50, choices=[("invoice","Invoice"),("leave","Leave")])
    sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.due_date}"
