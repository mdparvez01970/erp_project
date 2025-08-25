from rest_framework import serializers
from .models import Employee, Payslip
from datetime import date

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError("Salary must be greater than zero.")
        return value

    def validate_joining_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Joining date cannot be in the future.")
        return value

class PayslipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payslip
        fields = '__all__'
        
    def validate_basic(self, value):
        if value < 0:
            raise serializers.ValidationError("Basic salary cannot be negative.")
        return value

    def validate_allowance(self, value):
        if value < 0:
            raise serializers.ValidationError("Allowance cannot be negative.")
        return value

    def validate_deduction(self, value):
        if value < 0:
            raise serializers.ValidationError("Deduction cannot be negative.")
        return value

    def validate_net_salary(self, value):
        if value < 0:
            raise serializers.ValidationError("Net salary cannot be negative.")
        return value

    def validate_month(self, value):
        if value > date.today():
            raise serializers.ValidationError("Month cannot be in the future.")
        return value
