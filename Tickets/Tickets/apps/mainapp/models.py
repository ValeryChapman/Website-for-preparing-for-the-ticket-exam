from django.db import models


class Question(models.Model):
    option = models.IntegerField("Номер варианта", blank=True, null=False)
    banner = models.ImageField("Фотография", blank=True, null=True)


class Answer(models.Model):
    user = models.CharField("Автор ответа", blank=True,
                            null=True, max_length=50)
    description = models.TextField(
        "Текст ответа", blank=True, null=True, max_length=1000000)
    answer_question = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=False, related_name='answer_question')

    def __str__(self):
        return self.description
