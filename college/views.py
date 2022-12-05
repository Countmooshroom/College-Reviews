from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question


def index(request):
    choices = Choice.objects.all().values().order_by('-votes')
    questions = Question.objects.all().values()
    return render(request, 'college/index.html', {'choices': choices, 'questions': questions})
#class IndexView(generic.ListView):
#    template_name = 'college/index.html'
#    context_object_name = 'latest_question_list'
#
#    def get_queryset(self):
#        """Return the last five published questions."""
#        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'college/detail.html'


def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    choices = question.choice_set.all().order_by('-votes')
    total_votes = 0
    for i in choices:
        total_votes += i.votes
    return render(request, 'college/results.html', {'question': question, 'choices': choices, 'total_votes': total_votes})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'college/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('college:results', args=(question.id,)))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'college/detail.html', {'question': question})