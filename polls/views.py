from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Question


# def index(request):
#     # Retrieving Data
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # Retrieving Template
#     template = loader.get_template('polls/index.html')
#     # Setting the 'Context'
#     context = RequestContext(request, {
#         'latest_question_list': latest_question_list,
#     })
#
#     # Loading the appropriate template with the appropriate data.
#     return HttpResponse(template.render(context))
#     # Alternatively, we can use
#
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # context = {'latest_question_list': latest_question_list}
#     # return render(request, 'polls/index.html',context)
#
#
# def detail(request, question_id):
#     # TODO: Both of these return statement works.
#     # return HttpResponse("You're looking at question %s." % question_id)
#     # return HttpResponse("You are looking at question: "+question_id)
#
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
#
# def vote(request, question_id):
#
#     #request.POST returns something like a dictionary
#     p = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         #Will Raise Error if choice is not found in POST dictionary
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': p,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
#
#
# def raisingError(request):
#     raise Http404("Invalid Page")

# TODO: Templates Directory rshould be created.

# Generic Views
# List View: Abstract concept of listing the entire desired object.
# Detail View: Abstract Concept of Displaying detailed information an object
# Equivalent of Grail's Scaffolding

# MUST set the desired model.
# Detailed View requires pk to be captured from URL.
# By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html.
# the ListView generic view uses a default template called <app name>/<model name>_list.html;
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
    model = Question
    template_name = 'polls/results.html'
