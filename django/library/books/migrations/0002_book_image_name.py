# Generated by Django 4.0.6 on 2022-09-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image_name',
            field=models.ImageField(null=True, upload_to='book_images'),
        ),
    ]