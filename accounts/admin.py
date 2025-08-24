from django.contrib import admin
from .models import User, AccountHead, GeneralLedger

admin.site.register(User)
admin.site.register(AccountHead)
admin.site.register(GeneralLedger)
