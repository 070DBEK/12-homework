from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products_images/')
    category = models.CharField(max_length=100)

    def get_detail_url(self):
        return reverse('products:detail', args=[self.pk])
