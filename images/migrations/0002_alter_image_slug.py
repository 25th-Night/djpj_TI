# Generated by Django 4.2.3 on 2023-08-05 22:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="slug",
            field=models.SlugField(allow_unicode=True, blank=True, max_length=200),
        ),
    ]