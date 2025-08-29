from .models import ActivityLog

def log_activity(user, action, module, instance=None, changes=None):
    object_id = instance.pk if instance else None
    object_repr = str(instance) if instance else ''
    ActivityLog.objects.create(
        user=user,
        action=action,
        module=module,
        object_id=object_id,
        object_repr=object_repr,
        changes=changes
    )
