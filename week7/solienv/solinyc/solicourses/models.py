from django.db import models
from django.urls import reverse
# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    
    def get_absolute_url(self):
        return reverse("courses:courses-detail", kwargs={"id": self.id})