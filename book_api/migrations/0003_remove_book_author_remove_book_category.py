# Generated by Django 4.1.3 on 2022-11-04 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0002_book_author_book_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
    ]
