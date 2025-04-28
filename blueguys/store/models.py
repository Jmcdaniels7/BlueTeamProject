from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='items/', blank=True)
    stock = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100, blank=True, null=True)  

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
