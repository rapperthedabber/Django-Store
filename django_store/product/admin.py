from django.contrib import admin
from .models import Category,Product,productType

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(productType)