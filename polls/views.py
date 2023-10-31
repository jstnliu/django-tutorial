# from django.shortcuts import get_object_or_404, render

# #  Create your views here.
# #  HOW TO CREATE VIEWS 

# STEP 28: OVERHAUL VIEWS :)
# #  STEP 1.
# #  To call the view, we need to map it to a URL
# #  - and for this we need a URLconf.
# #  to create a URLconf in polls directory, create a file called 'urls.py' 
# #  which should also be in the 'polls' folder
# from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
# # STEP 15: no longer need 'loader', replace w/ 'render()'
# # from django.template import loader
# # STEP 17: import 'get_object_or_404()' shortcut
#     # - edit details again 
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse

# # STEP 12: Import Question Model
# from .models import Question
# # STEP 12.5: Rewrite 'index' views to
#     # - display latest 5 poll q's
#     # - they should be separated by commas (,)
#     # - and by publication date
# def index(request):
# # STEP 14: again, update index to take new html page
#     # import 'loader' above
#         # third:
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)        
#         # first:
#     # return HttpResponse('Hello, world. You\'re at the polls index.')
#         # second:
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
# # PROCEED TO/MAKE 'templates' directory/ 'polls' directory

# # STEP 10: add more views for further app functionality
# def detail(request, question_id):
# # STEP 16: handling '404 error
#     # - from simple 'return' response...
#     # return HttpResponse('You\'re looking at question %s.' % question_id)
#     # ...to:
#     # try: 
#     #     question = Question.objects.get(pk = question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404('Question does not exist.')
#     # return render(request, 'polls/detail.html', {'question': question})
#     # STEP 17.5:
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/detail.html', {'question': question})
# # Travel to detail.html

# def results(request, question_id):
#     # STEP 25: write in redirect to the results page for questions
#         # - add import get_object_or_404 to django.shortcuts
#     # was:
#     # response = 'You\'re looking at the results of question %s.'
#     # return HttpResponse(response % question_id)
#     # now: 
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
# # create results.html

# def vote(request, question_id):
#     # STEP 24: update vote for real functionality
#         #  - import 'HttpResponseRedirect
#         #  - import 'reverse' from 'django.urls'
#     # was: 
#     # return HttpResponse('You\'re voting on question %s.' % question_id)
#     # now:
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))