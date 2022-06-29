from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import Topic, Author, UserExt, Task, Lesson, Stage, Edge

import collections


########################### Topics ###########################

class TopicInline(admin.StackedInline):
    fields = ['name']
    model = Topic
    extra = 1


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    fields = ['name', 'supertopic']
    list_display = ('display_name', 'supertopic_name', 'topo_order')
    # readonly_fields = ('supertopic',)
    # list_select_related = ('supertopic',)

    inlines = [TopicInline]
    actions = ['topo_sort']

    @admin.action(description="Recompute topological order")
    def topo_sort(self, request, queryset):
        Topic.objects.get(name="__root__").topo_sort()


########################### Users ###########################

admin.site.unregister(User)


class UserExtInline(admin.StackedInline):
    model = UserExt
    fieldsets = (
        (None, {'fields': ('codeforces', 'infoarena', 'varena'), }),
        # ('Progress', {'fields': ('current_lesson',)}),
    )
    readonly_fields = ('codeforces', 'infoarena', 'varena')


@admin.register(User)
class UserCustomAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [UserExtInline]


########################### Authors ###########################

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'user']
    list_display = ('name', 'user_link')
    list_display_links = ('name', 'user_link')

    # In case you want to link an author to their account, comment this line
    readonly_fields = ('user',)

    def user_link(self, obj):
        if obj.user is None:
            return None
        return format_html("<a href='/admin/auth/user/{pk}'>{username}</a>", pk=obj.user.pk, username=obj.user)


########################### Tasks ###########################

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'description', 'task_link', 'solution_link')
    list_display_links = ('title', 'task_link', 'solution_link')
    fieldsets = (
        (None, {'fields': ('title', 'source', 'link', 'description', 'solution', 'tags')}),
        ('Hints', {
            'fields': ('hints', ('hint1', 'hint2', 'hint3')),
            'classes': ('collapse',),
        }),
    )

    def task_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)
    task_link.short_description = "Link to task"

    def solution_link(self, obj):
        if obj.solution is None:
            return None
        return format_html("<a href='{url}'>Solution</a>", url=obj.solution)
    solution_link.short_description = "Link to solution"


########################### Lessons ###########################

def topo_sort(stages=None):
    if stages is None:
        stages = Stage.objects.all().order_by('index')
    for stage in stages:
        start = []
        dep_count = {}

        for lesson in Lesson.objects.filter(stage=stage):
            if lesson.ins.filter(src__stage=stage).count() == 0:
                upper = 0
                for edge in lesson.ins.all():
                    upper = max(upper, edge.src.stage.index)
                start.append((lesson, upper))
                print(lesson, upper)
            else:
                dep_count[lesson] = lesson.ins.filter(src__stage=stage).count()
                # print(lesson, dep_count[lesson])

        print(start)
        q = collections.deque([x[0] for x in sorted(start, key=lambda item: item[1])])
        lvl = 0
        count_lvl = 0
        while q:
            node = q.popleft()

            if count_lvl == 3:
                lvl += 1
                count_lvl = 0
            else:
                for edge in node.ins.all():
                    dep = edge.src
                    if dep.stage == stage and dep.level == lvl:
                        lvl += 1
                        count_lvl = 0
                        break

            node.level = lvl
            node.save()
            count_lvl += 1

            for edge in node.outs.all():
                if edge.dest.stage == stage:
                    next = edge.dest
                    dep_count[next] -= 1
                    if dep_count[next] == 0:
                        q.append(next)


class LessonInline(admin.TabularInline):
    fields = ['src', 'hidden']
    model = Edge
    fk_name = 'dest'
    extra = 1


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'stage', 'topic', 'level', 'author')
    fieldsets = (
        (None, {'fields': (('title', 'author'), 'topic', 'stage', 'level')}),
        ('Content', {'fields': ('duration', 'content')}),
        ('Extra', {'fields': ('tasks',)}),
    )
    readonly_fields = ['level']
    inlines = [LessonInline]

    actions = ['topo_sort_all', 'topo_sort_stage']
    list_filter = ['stage', 'author']

    @admin.action(description="Recompute ALL topological order")
    def topo_sort_all(self, request, queryset):
        Lesson.objects.all().update(level=None)
        topo_sort()

    @admin.action(description="Recompute SINGLE topological order")
    def topo_sort_stage(self, request, queryset):
        stage = queryset.all()[0].stage
        Lesson.objects.filter(stage=stage).update(level=None)
        topo_sort([stage])


########################### Stages ###########################

# admin.site.register(Stage)

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('name', 'index')