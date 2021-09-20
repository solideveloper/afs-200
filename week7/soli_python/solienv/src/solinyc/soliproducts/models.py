from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
     title = models.CharField(max_length=120) # max_length required when using CharField
     description = models.TextField(blank=True, null=True)
     # blank has to do with how field is rendured, if blank=False then render is required
     # null has to do with database - just means it can be empty in db
     price = models.DecimalField(decimal_places=2, max_digits=10)
     summary = models.TextField(blank=False, null=False)
     # you can add models via migrations folder or in terminal with manage.py makemigrations
     featured = models.BooleanField(default=True) # null=True, default=True

     def get_absolute_url(self):
          return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"