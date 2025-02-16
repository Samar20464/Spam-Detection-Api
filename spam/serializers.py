from rest_framework import serializers
from .models import SpamReport

class SpamReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamReport
        fields = ['id', 'phone_number', 'reported_by', 'reported_at']
        read_only_fields = ['reported_by', 'reported_at']