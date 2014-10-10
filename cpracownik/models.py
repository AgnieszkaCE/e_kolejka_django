
from datetime import datetime
from django.db import models

from pokoje.models import Pokoj


# Create your models here.
class Info(models.Model):
    temat = models.CharField(max_length=50)
    tresc = models.CharField(max_length=50)
    data = models.DateTimeField(default=datetime.now, blank=True)
    p = models.ForeignKey(Pokoj,null=True,blank=True)
        
    class Meta:
        verbose_name = "Informacja"
        verbose_name_plural = "Informacje"
    
    def __unicode__(self):
        return self.temat
    