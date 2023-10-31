from django.urls import path 

from . import views

# STEP 21: to differentiate URL names 
    # - use what is called an app namespace
app_name = 'polls'
# travel to index.html
urlpatterns = [ 
    # STEP 27: update urlpatterns
    # # /polls/
    # path('', views.index, name = 'index'),
    # # STEP 11: Wire (route) new views 
    # # /polls/5/
    # # STEP 20: change URL to '/polls/specifics/5/'
    # path('specifics/<int:question_id>/', views.detail, name = 'detail'),
    # # polls/5/results/
    # path('<int:question_id>/results/', views.results, name = 'results'),
    # # /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name = 'vote'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

#  STEP 2
# next step, point the root URLconf at the 'polls.urls' module
# to do so, navigate to 'mysite/urls.py' 


