from rest_framework import serializers
from .models import TaxRule

class TaxRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxRule
        fields = '__all__'
