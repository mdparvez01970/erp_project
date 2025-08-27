from django.core.cache import cache
from .models import TaxRule

def get_tax_config():
    cache_key = "tax_config"
    config = cache.get(cache_key)
    if not config:
        config = list(TaxRule.objects.values())
        cache.set(cache_key, config, timeout=3600)
    return config
