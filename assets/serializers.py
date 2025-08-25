from rest_framework import serializers
from .models import Asset
from datetime import date

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'
        
        
    def validate_purchase_value(self, value):
        if value <= 0:
            raise serializers.ValidationError("Purchase value must be greater than 0.")
        return value

    def validate_purchase_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Purchase date cannot be in the future.")
        return value

    def validate_depreciation_rate(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Depreciation rate must be between 0 and 100.")
        return value
