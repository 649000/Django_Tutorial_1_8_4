from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404

from .models import Question


def index(request):
    #Retrieving Data
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #Retrieving Template
    template = loader.get_template('polls/index.html')
    #Setting the 'Context'
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })

    #Loading the appropriate template with the appropriate data.
    return HttpResponse(template.render(context))
    #Alternatively, we can use

    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    #return render(request, 'polls/index.html',context)

def detail(request, question_id):

    #TODO: Both of these return statement works.

    #return HttpResponse("You're looking at question %s." % question_id)
    return HttpResponse("You are looking at question: "+question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def raisingError(request):
    raise Http404("Invalid Page")


#TODO: Templates Directory rshould be created.
