from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Topic, Author, UserExt, Task, Lesson


########################### Topics ###########################

class TopicInline(admin.StackedInline):
    fields = ['name']
    model = Topic
    extra = 1


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    fields = ['name', 'supertopic']
    list_display = ('get_display_name', 'get_supertopic_name', 'topo_order')
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
        ('Progress', {'fields': ('current_lesson',)}),
    )
    readonly_fields = ('current_lesson', 'codeforces', 'infoarena', 'varena')


@admin.register(User)
class UserCustomAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [UserExtInline]


########################### Authors ###########################

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'user']
    list_display = ('name', 'user')

    # In case you want to link an author to their account, comment this line
    readonly_fields = ('user',)


########################### Tasks ###########################

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'source', 'link', 'description', 'solution')}),
        ('Hints', {
            'fields': ('hints', ('hint1', 'hint2', 'hint3')),
            'classes': ('collapse',),
        }),
    )


########################### Lessons ###########################

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': (('title', 'author'), 'topic', 'stage', 'dependencies')}),
        ('Content', {'fields': ('duration', 'content')}),
        ('Extra', {'fields': ('tasks',)}),
    )
