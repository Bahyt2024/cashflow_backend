from django.db import models
from django.conf import settings

class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # дата и время создания записи

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # дата и время создания записи

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)  # дата и время создания записи

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    created_at = models.DateTimeField(auto_now_add=True)  # дата и время создания записи

    def __str__(self):
        return self.name

class CashFlow(models.Model):
    account = models.ForeignKey('card.Account', on_delete=models.CASCADE, related_name='cashflows')  # связь с картой
    date = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='cashflows')
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='cashflows')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='cashflows')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, related_name='cashflows')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.type} - {self.amount} - {self.account.card_number}"
