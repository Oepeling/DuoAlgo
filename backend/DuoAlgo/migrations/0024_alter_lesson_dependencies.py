# Generated by Django 4.0.4 on 2022-06-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DuoAlgo', '0023_remove_userext_completed_lessons_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='dependencies',
            field=models.ManyToManyField(blank=True, related_name='rev_dep', related_query_name='rev_dep', to='DuoAlgo.lesson', verbose_name='Things to learn before'),
        ),
    ]