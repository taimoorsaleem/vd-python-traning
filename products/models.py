from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.CharField(max_length=250)
    price = models.IntegerField()
    rating = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE,)

    def __str__(self):
      return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
      return self.name