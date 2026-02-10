from django.db import models

class UrlData(models.Model):
    url = models.URLField(max_length=200)
    slug = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.slug} → {self.url}"
