from django.contrib import admin
from .models import SpamReport

@admin.register(SpamReport)
class SpamReportAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'reported_by', 'reported_at')
    search_fields = ('phone_number',)