from django.db import models


class Alcohol(models.Model):
    """An alcohol kind model for each drink"""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Drink(models.Model):
    """a peoduct model that inclouds the details of the products"""

    name = models.CharField(max_length=50)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
