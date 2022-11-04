from django.db import models


# Create your models here.
class Author(models.Model):
    fullName = models.CharField(max_length=255)
    biography = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.fullName

