from rest_framework import serializers
from .models import TaxRule

class TaxRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxRule
        fields = '__all__'
        
    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Tax rule name must be at least 2 characters long.")
        return value

    def validate_rate(self, value):
        if value < 0:
            raise serializers.ValidationError("Tax rate cannot be negative.")
        return value

    def validate_type(self, value):
        if value not in ['VAT', 'GST', 'Income']:
            raise serializers.ValidationError("Invalid tax type.")
        return value
