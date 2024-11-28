# Generated by Django 5.1.3 on 2024-11-28 04:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Museum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('categories', models.ManyToManyField(related_name='museums', to='post.category')),
            ],
        ),
    ]
