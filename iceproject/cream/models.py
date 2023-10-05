from django.db import models

# Create your models here.
class Larek(models.Model):
    larek_name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.larek_name
    
class IceCream(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=1,max_digits=1000,default=500)
    larek = models.ForeignKey(Larek,on_delete=models.CASCADE,related_name='larek')
    
    def __str__(self):
        return self.name