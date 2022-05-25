from django.contrib import admin
from .models import Topic


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