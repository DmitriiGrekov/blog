# Generated by Django 3.0.8 on 2020-07-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('keyword', models.TextField(verbose_name='Ключевые слова')),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('answer', models.TextField(default=None)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]
