from django.db import models

class House(models.Model):
    
    """ Model Definition for Houses """
    
    name = models.CharField(max_length=200)
    price_per_night = models.PositiveIntegerField(verbose_name="Price")
    description = models.TextField()
    address = models.CharField(max_length=200)
    pets_allowed = models.BooleanField(default=True, help_text="Are pets allowed?")
    
    def __str__(self):
        return self.name