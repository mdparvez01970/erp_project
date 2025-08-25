from rest_framework import serializers
from .models import Supplier, PurchaseInvoice
from datetime import date

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        
    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Supplier name must be at least 2 characters long.")
        return value

class PurchaseInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoice
        fields = '__all__'
        
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value

    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value
