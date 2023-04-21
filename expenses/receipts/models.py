from django.db import models
from django.contrib.auth.models import User


USER = User
# Create your models here.


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        USER, related_name='categories', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Receipt(models.Model):
    vendor = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=15 ,decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    purchaser = models.ForeignKey(
        USER, related_name='receipts', on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        ExpenseCategory, related_name='receipts', on_delete=models.CASCADE
    )
    account = models.ForeignKey(
        Account, related_name='receipts', on_delete=models.CASCADE(null=True)
    )
