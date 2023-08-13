from django.db import models
from PIL import Image

from django.core.files import File
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

   
    
class Product(models.Model):
        category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
        name = models.SlugField()
        description = models.TextField()
        price = models.DecimalField(max_digits=200, decimal_places=2)
        date = models.DateTimeField(auto_now_add= True)
        
        class Meta:
         ordering = ('name',)

        def __str__(self):
            return self.name
    
        def get_absolute_url(self):
            return f'/{self.category.slug}/{self.slug}/'
        
        