from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Category(models.Model):

    name=models.CharField(max_length=250,db_index=True)
    slug=models.SlugField(max_length=250,db_index=True,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:index_category', args=[self.slug])


class Product(models.Model):

    category=models.ForeignKey(Category,related_name='products')
    name=models.CharField(max_length=250,db_index=True)

    slug=models.SlugField(max_length=250,db_index=True)
    image=models.ImageField(upload_to='product/%Y/%m/%d',blank=True)
    description=models.TextField(blank=True)
    available=models.BooleanField(default=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),) #

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])