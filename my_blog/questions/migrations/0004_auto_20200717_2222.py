# Generated by Django 3.0.8 on 2020-07-17 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_questionsmodel_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsmodel',
            name='answer',
            field=models.TextField(blank=True),
        ),
    ]
