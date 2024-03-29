# Generated by Django 3.0.2 on 2022-05-21 14:27

import DuoAlgo.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Author name')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Stage name')),
                ('index', models.IntegerField(unique=True, verbose_name='Stage index')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Task title')),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='Task description (optional)')),
                ('link', models.URLField(verbose_name='Link to task')),
                ('solution', models.URLField(blank=True, default=None, null=True, verbose_name='Link to solution (optional)')),
                ('hints', models.BooleanField(default=False, verbose_name='Does it have a hint system?')),
                ('hint1', models.TextField(blank=True, default=None, null=True, verbose_name='First hint')),
                ('hint2', models.TextField(blank=True, default=None, null=True, verbose_name='Second hint')),
                ('hint3', models.TextField(blank=True, default=None, null=True, verbose_name='Third hint')),
            ],
        ),
        migrations.CreateModel(
            name='UserExt',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('codeforces', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Codeforces handle')),
                ('infoarena', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Infoarena username')),
                ('varena', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Varena username')),
                ('completed_lessons', models.ManyToManyField(related_name='done', to='DuoAlgo.Lesson', verbose_name='Already done')),
                ('current_lesson', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current', to='DuoAlgo.Lesson', verbose_name='Current lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Topic name')),
                ('supratopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DuoAlgo.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='stage',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=DuoAlgo.models.Stage, to='DuoAlgo.Stage'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='topic',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=DuoAlgo.models.Topic, to='DuoAlgo.Topic'),
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dest', to='DuoAlgo.Lesson')),
                ('src_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='src', to='DuoAlgo.Lesson')),
            ],
        ),
    ]
