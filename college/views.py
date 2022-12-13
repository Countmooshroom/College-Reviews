from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question, Teacher


def index(request):
    choices = Choice.objects.all().values().order_by('-votes')
    questions = Question.objects.all().values()
    return render(request, 'college/index.html', {'choices': choices, 'questions': questions})


def courses(request):
    questions = Question.objects.all().values()
    departments = []
    for q in questions:
        departments.append(q['question_text'][:4])
    departments = sorted(list(dict.fromkeys(departments)))#remove duplicates and sort
    return render(request, 'college/courses.html', {'questions': questions, 'departments': departments})


def department(request, dept):
    questions = Question.objects.all().values().order_by('question_text')
    courses = []
    for course in questions:
        if course['question_text'].startswith(dept):
            courses.append(course)
    return render(request, 'college/department.html', {'dept': dept, 'courses': courses})


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
        return HttpResponseRedirect(reverse('college:results', args=(question.id,)))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'college/detail.html', {'question': question})

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        print('search')
        post = Teacher.objects.all().filter(name__contains=search)
        return render(request, 'searchbar.html', {'post': post})