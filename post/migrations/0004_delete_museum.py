# Generated by Django 5.1.3 on 2024-11-28 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_image_url_post_location'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Museum',
        ),
    ]
