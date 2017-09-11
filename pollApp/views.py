from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone
import datetime


class IndexView(generic.ListView):
    template_name = 'pollApp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        
        # get the last five questions

        return Question.objects.filter( pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'pollApp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'pollApp/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        # Showing the question voting form again

        return render(request, 'pollApp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('pollsNamespace:resultsName', args=(question.id,)))

