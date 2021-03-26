from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='main__page'),
    path('answer/<str:pk>/', AnswerPageView.as_view(), name='answer__page'),
]
