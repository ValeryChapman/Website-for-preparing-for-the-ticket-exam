from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from .models import *


class MainPageView(TemplateView):
    template_name = "main.html"
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = Question.objects.all().order_by('option')
        return context


class AnswerPageView(ListView):
    template_name = "qw-page.html"
    queryset = Answer
    context_object_name = 'answer'

    def get_queryset(self):
        return Answer.objects.filter(answer_question=Question.objects.get(id=self.kwargs['pk']))

    def get_context_data(self, **kwargs):
        context = super(AnswerPageView, self).get_context_data(**kwargs)
        context['question'] = Question.objects.get(id=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        data = self.request.POST
        question = Question.objects.get(id=kwargs['pk'])
        model = Answer.objects.create(
            user=data['user'], description=data['description'], answer_question=question).save()
        return redirect('answer__page', question.id)
