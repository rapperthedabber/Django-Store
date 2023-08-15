#building tables 
#build classes to map it and turn it into tables 
from django.db import models 
from django.urls import reverse 
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

class Category(models.Model):
    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=("Required and Unique"),
        max_length=255,
        blank=True
    )

    #slug is a addressable url string 
    slug = models.SlugField(verbose_name=_("Category safe URL"), max_length=255 , unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)

    # class MPTTMeta:
    #     order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])
    
    def __str__(self):
        return self.name


class productType(models.Model):

    name = models.CharField(verbose_name=_("Product Name"), help_text=_("Required"), max_length=225)
    isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self):
        return self.name


class productSpecification(models.Model):
    product_type = models.ForeignKey(productType, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=("Name"), help_text=("Required"), max_length=255)
    class Meta:
        verbose_name= _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def _str_(self):
       return self.name

class Product(models.Model):
    product_type = models.ForeignKey(productType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    title = models.CharField(verbose_name=("title"),help_text=_("required"), max_length=255, blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("Regular Price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name":{
                "max_length": _("The price must be between 0 and 999.99")
            },
        },
        max_digits=5,
        decimal_places=2)
    
    is_active = models.BooleanField(
        verbose_name=("Product Visibility"),
        help_text=("Change product visibility"),
        default=True,
    )

    
    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def get_absolute_url(self):
        return reverse("storefront:product_detail", args={self.slug})
    
    def _str_(self):
        return self.title
    
class productSpecificationValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(productSpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=_("value"),
        help_text=_("product specification value (maximum of 255 words)"),
        max_length=255,
    )
    class Meta:
        verbose_name =_("Product specification"), 
        verbose_name_plural = ("Product specifications"  )
    
    def _str_(self):
        return self.value
    

class productImage(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    image = models.CharField(
        verbose_name=_("image"),
        help_text=("Please add a image"),
        max_length=255,
        null=True,
        blank=True,
    )

    is_feature = models.BooleanField(default = False)
    created_at = models.DateField(auto_now_add=True, editable=False)
    
    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")


    