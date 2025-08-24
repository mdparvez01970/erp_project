from django.contrib import admin
from .models import Customer, SalesInvoice

admin.site.register(Customer)
admin.site.register(SalesInvoice)
