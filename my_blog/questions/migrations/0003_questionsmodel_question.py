# Generated by Django 3.0.8 on 2020-07-17 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20200717_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionsmodel',
            name='question',
            field=models.TextField(default=1, verbose_name='Вопрос'),
            preserve_default=False,
        ),
    ]