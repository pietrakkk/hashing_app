
from django.db import models


class HashedUrl(models.Model):
    hash_value = models.CharField(max_length=15, unique=True)
    url = models.URLField()

    def __unicode__(self):
        return '{}, {}'.format(self.hash_value, self.url)
