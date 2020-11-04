
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: HOST/polls/
    path('', views.index, name='index'),
    # ex: HOST/polls/5/
    # the 'name' value is called by the {% url %} template tag
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: HOST/polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: HOST/polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
