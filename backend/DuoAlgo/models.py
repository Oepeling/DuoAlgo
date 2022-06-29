from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from django.db.models.signals import post_save, pre_save


# in admin
class Topic(models.Model):
    name = models.CharField("Topic name", max_length=100)
    supertopic = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    topo_order = models.CharField(max_length=20, blank=True, default="")
    full_name = models.CharField(max_length=100, blank=True, default="")

    def display_name(self):
        return "\\ " * len(self.topo_order) + self.name

    def __str__(self):
        return self.full_name

    def supertopic_name(self):
        if self.supertopic is None:
            return ""
        else:
            return self.supertopic.name

    def get_subtopics(self):
        return Topic.objects.filter(supertopic=self)

    def count_subtopics(self):
        return self.get_subtopics().count()

    def topo_sort(self, order="", path="~"):
        if self.supertopic is not None:
            path = path + " / " + self.name

        self.full_name = path
        self.topo_order = order
        self.save()

        for index, subtopic in enumerate(self.get_subtopics()):
            subtopic.topo_sort(order + chr(index + 97), path)

    @classmethod
    def post_create(cls, sender, instance, created, *args, **kwargs):
        if not created:
            return

        just_added_padre = -1
        if instance.supertopic is None:
            instance.supertopic = Topic.objects.get(name="__root__")
            just_added_padre = 0

        instance.topo_order = instance.supertopic.topo_order \
                              + chr(just_added_padre + instance.supertopic.count_subtopics() + 97)
        instance.save()

    class Meta:
        ordering = ['topo_order']


post_save.connect(Topic.post_create, sender=Topic)


# in admin
# todo: add topics?
class Task(models.Model):
    title = models.CharField("Task title", max_length=50)
    source = models.CharField("Task source", max_length=50)
    description = models.TextField("Task description (optional)", blank=True, null=True, default=None)
    link = models.URLField("Link to task", unique=True)
    solution = models.URLField("Link to solution (optional)", blank=True, null=True, default=None)

    tags = models.TextField("Tags (for now)", blank=True)

    hints = models.BooleanField("Does it have a hint system?", default=False)
    hint1 = models.TextField("First hint", blank=True, null=True, default=None)
    hint2 = models.TextField("Second hint", blank=True, null=True, default=None)
    hint3 = models.TextField("Third hint", blank=True, null=True, default=None)

    def __str__(self):
        if self.source is None:
            return self.title
        return self.title + " (" + self.source + ")"


# todo: make one-to-one
# in admin
class Author(models.Model):
    name = models.CharField("Author name", max_length=50)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,
                             verbose_name="User account (if exists)")

    def __str__(self):
        return self.name


# in admin
class Stage(models.Model):
    name = models.CharField("Stage name", max_length=50)
    index = models.IntegerField("Stage index", unique=True)

    def __str__(self):
        return self.name + "(" + str(self.index) + ")"


# in admin
class Lesson(models.Model):
    # todo: change defaults
    topic = models.ForeignKey("Topic", Topic, blank=True, null=True, default=None)
    stage = models.ForeignKey("Stage", Stage)
    level = models.PositiveIntegerField("Level in stage", blank=True, null=True, default=None)

    title = models.CharField("Title", max_length=100)
    author = models.ForeignKey(Author, models.SET_NULL, blank=True, null=True, default=None, verbose_name="Author")

    duration = models.DurationField("Lesson duration (optional)", blank=True, null=True, default=None)
    content = MDTextField("Lesson content in .md format", blank=True, null=True)
    # body = models.TextField("Lesson body in .md format", blank=True, null=True)
    link_to_code = models.URLField("Link to sample of code", blank=True, null=True, default=None)

    tasks = models.ManyToManyField(Task, verbose_name="List of related tasks", blank=True)

    def __str__(self):
        return self.title + " (" + self.stage.name + ")"

    class Meta:
        order_with_respect_to = 'stage'


class Edge(models.Model):
    src = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="outs")
    dest = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="ins")
    hidden = models.BooleanField(verbose_name="Hidden", default=False)


# in admin
class UserExt(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, verbose_name="User")

    codeforces = models.CharField("Codeforces handle", max_length=50, blank=True, null=True, default=None)
    infoarena = models.CharField("Infoarena username", max_length=50, blank=True, null=True, default=None)
    varena = models.CharField("Varena username", max_length=50, blank=True, null=True, default=None)

    def __str__(self):
        return self.user.__str__()


class DoneTasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Task")


class CompletedLessons(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Lesson")
    in_progress = models.BooleanField(verbose_name="Still in progress", default=False)