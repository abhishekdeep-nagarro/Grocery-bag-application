from django.db import models

# Create your models here.
class GROCERY(models.Model):
    status_choices = [
        ('B', 'BOUGHT'),
        ('NA', 'NOT AVAILABLE'),
        ('P', 'PENDING'),
    ]
    name = models.CharField(max_length=122)
    quantity = models.CharField(max_length=50)
    status = models.CharField(max_length=3, choices=status_choices)
    date = models.DateField()
