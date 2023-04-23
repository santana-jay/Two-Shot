from django.shortcuts import render,get_object_or_404, redirect
from receipts.models import ExpenseCategory,Receipt,Account

# Create your views here.

def receipt_list(request):
    receipt = Receipt.objects.all()
    context = {
        "receipt": receipt
    }
    return render(request, 'receipts/list.html', context)
