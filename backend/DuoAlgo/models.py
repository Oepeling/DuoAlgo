from django.db import models


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
    topic = models.ForeignKey("Topic", Topic, models.SET_NULL, blank=True, null=True)
    stage = models.ForeignKey("Stage", Stage, models.SET_NULL, blank=True, null=True)

    title = models.CharField("Title", max_length=100)
    author = models.ForeignKey("Credits to:", Author, models.SET_NULL, blank=True, null=True, default=None)

    duration = models.DurationField("Lesson duration (optional)", blank=True, null=True, default=None)
    body = models.TextField("Lesson body in .md format", blank=True, null=True)
    link_to_code = models.URLField("Link to sample of code", blank=True, null=True, default=None)

    tasks = models.ManyToManyField("List of related tasks", Task)


class Edge(models.Model):
    src_node = models.ForeignKey(Lesson)
    dest_node = models.ForeignKey(Lesson)

    # todo: add verification


class UserExt(models.User):
    class Meta:
        proxy = True

    codeforces = models.CharField("Codeforces handle", max_length=50, blank=True, null=True, default=None)
    infoarena = models.CharField("Infoarena username", max_length=50, blank=True, null=True, default=None)
    varena = models.CharField("Varena username", max_length=50, blank=True, null=True, default=None)

    completed_lessons = models.ManyToManyField("Already done", Lesson)
    current_lesson = models.ForeignKey("Current lesson", Lesson, blank=True, null=True, default=None)