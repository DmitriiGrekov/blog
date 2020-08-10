# Generated by Django 3.0.8 on 2020-08-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0004_books_meta_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='meta_keywords',
            field=models.CharField(default=1, max_length=255, verbose_name='Meta Keywords'),
            preserve_default=False,
        ),
    ]