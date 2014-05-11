from django.db import models
from django.contrib.auth.models import User
from pokoje.models import Pokoj

# Create your models here.
class Zapis(models.Model):
    id_user = models.ForeignKey(User)
    id_pokoj = models.ForeignKey(Pokoj)
    numerek = models.IntegerField()
    
    def _str_(self):
        return self.numerek
 
    def was_published_recently(self):
        return Zapis.objects.order_by('-numerek')[:1]
    was_published_recently.admin_order_field = 'numerek'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'