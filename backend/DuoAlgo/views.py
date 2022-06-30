from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from .models import Lesson


def index(request):
    return HttpResponse("Work in progress.")


def get_lessons(request):
    lessons = []
    for lesson in Lesson.objects.all():
        # lessons[str((lesson.stage.index, lesson.level))] = {
        lessons.append({
            'id': lesson.id,
            'title': lesson.title,
            'author': lesson.author.__str__(),
            'stage': lesson.stage.index,
            'level': lesson.level,
            'topic': lesson.topic.__str__(),
            'duration': lesson.duration
        })
    return JsonResponse({'lesson_list': lessons})


def get_lesson_info(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    return JsonResponse({'lesson': {
        'id': lesson.id,
        'title': lesson.title,
        'author': lesson.author.__str__(),
        'stage': lesson.stage.index,
        'level': lesson.level,
        'topic': lesson.topic.__str__(),
        'duration': lesson.duration,
        'content': lesson.content,
        'link_to_code': lesson.link_to_code,
        'dependencies': [x.src.id for x in lesson.ins.all()],
        'tasks': [x.id for x in lesson.tasks.all()]
    }})
