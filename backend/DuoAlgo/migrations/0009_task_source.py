# Generated by Django 4.0.4 on 2022-06-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DuoAlgo', '0008_alter_lesson_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='source',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Task source'),
        ),
    ]