# Generated by Django 3.0.8 on 2020-08-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_questionsmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsmodel',
            name='name',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
    ]