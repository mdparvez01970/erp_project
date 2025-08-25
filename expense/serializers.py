from rest_framework import serializers
from .models import Expense
from datetime import date

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
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
        valid_categories = dict(Expense.CATEGORY_CHOICES).keys()
        if value not in valid_categories:
            raise serializers.ValidationError("Invalid category.")
        return value
