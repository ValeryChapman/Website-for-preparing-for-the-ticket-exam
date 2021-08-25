from django.contrib import admin
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['option', 'banner']
    search_fields = ['option']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'answer_question']
    list_filter = ['answer_question']
    search_fields = ['user', 'text', 'answer_question']
    