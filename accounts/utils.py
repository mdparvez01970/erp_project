from django.core.cache import cache
from .models import AccountHead, GeneralLedger, ActivityLog
from django.db.models import Sum
from django.utils.timezone import now
from activity.models import ActivityLog


def log_activity(user, action, model_name, object_id=None, changes=None):
    ActivityLog.objects.create(
        user=user,
        action=action,
        model_name=model_name,
        object_id=object_id,
        changes=changes,
        timestamp=now()
    )

def get_account_report():
    cache_key = "account_report"
    report = cache.get(cache_key)
    if not report:
        accounts = AccountHead.objects.prefetch_related('generalledger_set').all()
        report = []
        for account in accounts:
            total_debit = account.generalledger_set.aggregate(total=Sum('debit'))['total'] or 0
            total_credit = account.generalledger_set.aggregate(total=Sum('credit'))['total'] or 0
            report.append({
                "account_code": account.code,
                "account_name": account.name,
                "account_type": account.type,
                "total_debit": total_debit,
                "total_credit": total_credit
            })
        cache.set(cache_key, report, timeout=600)  # 10 min
    return report

