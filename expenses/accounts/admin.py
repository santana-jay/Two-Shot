from django.contrib import admin
from receipts.models import ExpenseCategory, Receipt, Account


# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'number',
        'id'
    )

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'id'
    )

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = (
        'vendor',
        'total',
        'tax',
        'date',
        'id',
    )
