from django.contrib import admin
from .models import Topic

# todo: make topic create function so that no topic without supertopic can be created
admin.site.register(Topic)
