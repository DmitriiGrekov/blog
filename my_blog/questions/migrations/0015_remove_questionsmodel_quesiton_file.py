# Generated by Django 3.0.8 on 2020-07-21 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_auto_20200721_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionsmodel',
            name='quesiton_file',
        ),
    ]