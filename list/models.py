from django.db import models
from datetime import datetime, date
from django.db.models import Model

# Create your models here.
class List(models.Model):
    item = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=False, auto_now= False , blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    
    def datepublished(self):
        return self.published_date.strftime('%B %d %Y')

    def __str__(self):
        return self.item 
