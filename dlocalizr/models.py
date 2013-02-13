from django.db import models


class SharedUrl(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    ip = models.IPAddressField()
    user = models.SlugField()
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title
