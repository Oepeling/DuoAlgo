# Generated by Django 4.0.4 on 2022-06-12 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DuoAlgo', '0015_task_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='link',
            field=models.URLField(unique=True, verbose_name='Link to task'),
        ),
    ]
