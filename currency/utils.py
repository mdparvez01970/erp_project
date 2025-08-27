from django.core.cache import cache
from .models import Currency

def get_currency_rates():
    cache_key = "currency_rates"
    rates = cache.get(cache_key)
    if not rates:
        rates = {c.code: c.exchange_rate for c in Currency.objects.all()}
        cache.set(cache_key, rates, timeout=600)
    return rates
