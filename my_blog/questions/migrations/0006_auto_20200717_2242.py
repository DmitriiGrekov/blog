# Generated by Django 3.0.8 on 2020-07-17 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий к ответу', 'verbose_name_plural': 'Комментарии к ответу'},
        ),
    ]
