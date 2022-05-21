from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField("Task title", max_length=50)
    description = models.TextField("Task description (optional)", blank=True, null=True, default=None)
    link = models.URLField("Link to task")
    solution = models.URLField("Link to solution (optional)", blank=True, null=True, default=None)

    hints = models.BooleanField("Does it have a hint system?", default=False)
    hint1 = models.TextField("First hint", blank=True, null=True, default=None)
    hint2 = models.TextField("Second hint", blank=True, null=True, default=None)
    hint3 = models.TextField("Third hint", blank=True, null=True, default=None)


class Topic(models.Model):
    name = models.CharField("Topic name", max_length=100)
    supratopic = models.ForeignKey('self', on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField("Author name", max_length=50)


class Stage(models.Model):
    name = models.CharField("Stage name", max_length=50)
    index = models.IntegerField("Stage index", unique=True)


class Lesson(models.Model):
    # todo: change defaults
    topic = models.ForeignKey("Topic", Topic, blank=True, null=True, default=None)
    stage = models.ForeignKey("Stage", Stage, blank=True, null=True, default=None)

    title = models.CharField("Title", max_length=100)
    author = models.ForeignKey(Author, models.SET_NULL, blank=True, null=True, default=None, verbose_name="Credits to:")

    duration = models.DurationField("Lesson duration (optional)", blank=True, null=True, default=None)
    body = models.TextField("Lesson body in .md format", blank=True, null=True)
    link_to_code = models.URLField("Link to sample of code", blank=True, null=True, default=None)

    tasks = models.ManyToManyField(Task, verbose_name="List of related tasks")


class Edge(models.Model):
    src_node = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="src")
    dest_node = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="dest")

    # todo: add verification


class UserExt(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, verbose_name="User")

    codeforces = models.CharField("Codeforces handle", max_length=50, blank=True, null=True, default=None)
    infoarena = models.CharField("Infoarena username", max_length=50, blank=True, null=True, default=None)
    varena = models.CharField("Varena username", max_length=50, blank=True, null=True, default=None)

    completed_lessons = models.ManyToManyField(Lesson, related_name="done", verbose_name="Already done")
    current_lesson = models.ForeignKey(Lesson, blank=True, null=True, default=None, on_delete=models.SET_NULL,
                                       related_name="current", verbose_name="Current lesson")