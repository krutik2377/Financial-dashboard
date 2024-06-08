from django.contrib import admin
from .models import FinancialRecord

@admin.register(FinancialRecord)
class FinancialRecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'timestamp')
