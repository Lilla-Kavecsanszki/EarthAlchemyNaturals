from django.db import models


class Herb(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    benefits = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
