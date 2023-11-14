from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default='')
    description = models.TextField()
    photo = models.ImageField(upload_to='item_photos/', null=True, blank=True)
    
    def __str__(self):
        return self.name