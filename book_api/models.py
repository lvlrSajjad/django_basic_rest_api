from django.db import models


# Create your models here.
from author_api.models import Author
from category_api.models import Category


class Book(models.Model):
    title = models.CharField(max_length=255)
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

