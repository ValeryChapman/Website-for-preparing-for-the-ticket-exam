from django.db import models


class Question(models.Model):
    option = models.IntegerField("Номер варианта", unique=True)
    banner = models.ImageField("Фотография")

    def __str__(self):
        return f'Вариант #{self.option}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        
        
class Answer(models.Model):
    user = models.CharField("Автор ответа", max_length=50)
    text = models.TextField("Текст ответа", max_length=1000000, blank=True)
    answer_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_question')

    def __str__(self):
        return f'Ответ ({self.user} -> {self.answer_question})'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'