# Generated by Django 4.1.3 on 2022-11-04 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author_api', '0001_initial'),
        ('category_api', '0001_initial'),
        ('book_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='author_api.author'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='category_api.category'),
        ),
    ]
