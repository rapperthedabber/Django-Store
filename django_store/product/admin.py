from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category,Product,productType, productSpecification, productImage,productSpecificationValue

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(productType)

class ProductSpecificationInLine(admin.TabularInline):
    model = productSpecification

class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInLine,
    ]

class productImageSpecification(admin.TabularInline):
        model = productImage

class productSpecificationValueInline(admin.TabularInline):
     model = productSpecificationValue


class ProductAdmin(admin.ModelAdmin):
     inlines = [
          productSpecificationValue,
          productImageSpecification
     ]
  