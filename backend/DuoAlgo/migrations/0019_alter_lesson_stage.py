# Generated by Django 4.0.4 on 2022-06-25 21:43

import DuoAlgo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DuoAlgo', '0018_alter_lesson_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='stage',
            field=models.ForeignKey(default=1, on_delete=DuoAlgo.models.Stage, to='DuoAlgo.stage'),
            preserve_default=False,
        ),
    ]
