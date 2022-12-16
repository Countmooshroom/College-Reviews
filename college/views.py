from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Course


def index(request):
    choices = Choice.objects.all().values().order_by('-votes')
    courses = Course.objects.all().values()
    return render(request, 'college/index.html', {'choices': choices, 'courses': courses})


def courses(request):
    courses = Course.objects.all().values()
    departments = []
    for c in courses:
        departments.append(c['course_name'][:4])
    departments = sorted(list(dict.fromkeys(departments)))#remove duplicates and sort
    return render(request, 'college/courses.html', {'courses': courses, 'departments': departments})


def department(request, dept):
    courses = Course.objects.all().values().order_by('course_name')
    course_list = []
    for course in courses:
        if course['course_name'].startswith(dept):
            course_list.append(course)
    return render(request, 'college/department.html', {'dept': dept, 'courses': course_list})


def course(request, dept, name):
    course = get_object_or_404(Course, course_name=name)
    choices = course.choice_set.all().order_by('-votes')
    total_votes = 0
    for i in choices:
        total_votes += i.votes
    return render(request, 'college/course.html', {'course': course, 'choices': choices, 'total_votes': total_votes})


def vote(request, dept, name):
    course = get_object_or_404(Course, course_name=name)
    return render(request, 'college/course_vote.html', {'course': course})


def save(request, dept, name):
    course = get_object_or_404(Course, course_name=name)
    try:
        selected_choice = course.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'college/course_vote.html', {
            'course': course,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('college:course', args=('X', course.course_name,)))

def about(request):
    return render(request, 'college/about.html')