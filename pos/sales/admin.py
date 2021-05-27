from django.contrib import admin
from .models import Customer, MembershipType, Item

# Register your models here.
admin.site.register(Customer)
admin.site.register(MembershipType)
admin.site.register(Item)