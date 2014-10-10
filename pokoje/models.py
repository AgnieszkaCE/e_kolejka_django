from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pokoj(models.Model):
    nazwa = models.CharField(max_length=50)
    informacje = models.CharField(max_length=500)
    
    class Meta:
        verbose_name = "Pokoj"
        verbose_name_plural = "Pokoje"
        
    def __unicode__(self):
        return self.nazwa
    
class Numer(models.Model):
    id_user = models.ForeignKey(User)
    id_pokoj = models.ForeignKey(Pokoj)
    numerek = models.IntegerField()
 
    
    class Meta:
        verbose_name = "Numer"
        verbose_name_plural = "Numery"
    
    def __unicode__(self):
        return self.numerek

    