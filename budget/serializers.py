from rest_framework import serializers
from .models import Budget
from datetime import date

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
        
    def validate_allocated_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Allocated amount must be greater than 0.")
        return value

    def validate_spent_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Spent amount cannot be negative.")
        return value

    def validate(self, data):
        if data['spent_amount'] > data['allocated_amount']:
            raise serializers.ValidationError({
                "spent_amount": "Spent amount cannot exceed allocated amount."
            })
        if data['end_date'] < data['start_date']:
            raise serializers.ValidationError({
                "end_date": "End date cannot be earlier than start date."
            })
        if data['start_date'] > date.today():
            raise serializers.ValidationError({
                "start_date": "Start date cannot be in the future."
            })
        return data
