
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: HOST/polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: HOST/polls/5/
    # the 'name' value is called by the {% url %} template tag
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: HOST/polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: HOST/polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
