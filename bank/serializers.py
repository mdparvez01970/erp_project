from rest_framework import serializers
from .models import BankAccount, Transaction
from datetime import date

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'
        
    def validate_balance(self, value):
        if value < 0:
            raise serializers.ValidationError("Balance cannot be negative.")
        return value

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Transaction amount must be greater than 0.")
        return value

    def validate_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Transaction date cannot be in the future.")
        return value

    def validate(self, data):
        # Withdraw or transfer should not exceed balance
        if data['type'] in ['withdraw', 'transfer']:
            account = data['bank_account']
            if account.balance < data['amount']:
                raise serializers.ValidationError("Insufficient balance for this transaction.")
        return data
