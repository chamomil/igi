# Generated by Django 4.2.1 on 2023-06-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='catalog/static/catalog/posters/'),
        ),
    ]
