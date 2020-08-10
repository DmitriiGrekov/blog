# Generated by Django 3.0.8 on 2020-08-10 19:12

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('questions', '0018_auto_20200808_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsmodel',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Ключевые слова'),
        ),
    ]
