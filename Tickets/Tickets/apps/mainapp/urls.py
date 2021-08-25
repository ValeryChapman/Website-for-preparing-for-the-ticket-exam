from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^/?$', MainPageView.as_view(), name='main__page'),
    re_path(r'^answer/(?P<pk>\w+)/?$', AnswerPageView.as_view(), name='answer__page')
]
