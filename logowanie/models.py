from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode

class Logowanie(models.Model):

    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,

    )

    email = models.EmailField()

    owner = models.ForeignKey(User)

    def __unicode__(self):
        return smart_unicode(" ".join([self.first_name, self.last_name]))

    def get_absolute_url(self):

        return reverse('index', kwargs={'pk': self.id})
