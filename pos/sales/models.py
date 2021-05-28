from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.
class MembershipType(models.Model):
    name = models.CharField(max_length=20, help_text="Enter membership type (e.g. Associate, Full, etc.)")

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Customer(models.Model):
    prefix = models.CharField(max_length=6, null=True, blank=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    suffix = models.CharField(max_length=4, null=True, blank=True)
    date_joined = models.DateField(null=True, blank=True)
    member_type = models.ForeignKey(MembershipType, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular customer instance."""
        return reverse('customer-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Item(models.Model):
    code = models.SmallIntegerField(help_text="Numeric code field", unique=True)
    name = models.CharField(max_length=60, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_taxable = models.BooleanField(default=False)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.name

class Transaction(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    sold_on = models.DateField(auto_now_add=True)

class TransactionDetail(models.Model):
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.RESTRICT)
    quantity = models.SmallIntegerField
