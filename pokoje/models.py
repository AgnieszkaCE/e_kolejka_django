from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pokoj(models.Model):
    nazwa = models.CharField(max_length=50)
    informacje = models.CharField(max_length=500)
    
    def _str_(self):
        return self.nazwa
    
class Numer(models.Model):
    id_user = models.ForeignKey(User)
    id_pokoj = models.ForeignKey(Pokoj)
    numerek = models.IntegerField()
    
    def _str_(self):
        return self.numerek

    