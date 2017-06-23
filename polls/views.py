# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import Choice, Question
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	selected_choice = question.choice_set.get(pk=request.POST['choice'])
	selected_choice.votes += 1
	selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
