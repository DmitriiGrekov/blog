# Generated by Django 3.0.8 on 2020-08-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_servicepost_meta_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepost',
            name='meta_keywords',
            field=models.CharField(default=1, max_length=255, verbose_name='Мета ключевые слова'),
            preserve_default=False,
        ),
    ]