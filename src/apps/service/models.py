from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.core.models import BaseModel
# Create your models here.

class ServiceModel(models.Model):
    name = models.CharField(max_length=150,verbose_name='Service')
    description_about = models.TextField(verbose_name='Description About Service')
    description_product = models.TextField(verbose_name='Description Product Service')
    image = models.ImageField(upload_to='services/images/',null=True,blank=True,
                              verbose_name='Service Image')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class CategoryModel(models.Model):
    service = models.ForeignKey(ServiceModel,on_delete=models.CASCADE,
                                related_name='categories')
    name = models.CharField(max_length=150,verbose_name='Category Name')
    description = models.TextField(verbose_name='Category Description')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class ProductModel(BaseModel):
    category = ChainedForeignKey(CategoryModel,chained_field='service',chained_model_field='service',
                                 show_all=False,auto_choose=False,sort=True)
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE,
                                related_name='products')
    name = models.CharField(max_length=150,verbose_name="Product Name")
    description = models.TextField(verbose_name='Products Description')
    image = models.ImageField(upload_to="products/images/",null=True,blank=True
                              ,verbose_name="Product Image")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
