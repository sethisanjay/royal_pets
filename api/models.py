from django.db import models

# Create your models here.
class Product(models.Model):
    id= models.TextField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    rating=models.DecimalField(max_digits=2, decimal_places=1)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name