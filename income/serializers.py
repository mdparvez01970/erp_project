from rest_framework import serializers
from .models import Income
from datetime import date

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'
        
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value

    def validate_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Date cannot be in the future.")
        return value

    def validate_category(self, value):
        valid_categories = dict(Income.CATEGORY_CHOICES).keys()
        if value not in valid_categories:
            raise serializers.ValidationError("Invalid category.")
        return value
