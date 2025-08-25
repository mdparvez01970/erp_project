from rest_framework import serializers
from .models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'
        
    def validate_code(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Currency code must only contain letters (e.g., USD, BDT).")
        if len(value) < 3:
            raise serializers.ValidationError("Currency code must be at least 3 characters long.")
        return value.upper()

    def validate_exchange_rate(self, value):
        if value <= 0:
            raise serializers.ValidationError("Exchange rate must be greater than 0.")
        return value
