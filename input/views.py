from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from college.models import Course, Choice
from datetime import datetime

def add_class(request):
    return render(request, 'college/add_class.html')

def add_teacher(request, course_name):
    return render(request, 'college/add_teacher.html', {'course_name': course_name})

def save_class(request):
    name = request.POST['class-name']
    try:
        #check for course already exists
        course = Course.objects.get(course_name=name)
        return render(request, 'college/add_class.html', {'error_message': "This class already exists!",})
    except Course.DoesNotExist:
        #check for any text
        if name:
            try:
                if name[:3].isupper() and name[4] == ' ' and name[5:].isnumeric():
                    course = Course(course_name=name)
                    course.pub_date = datetime.now()
                    course.save()
                else:
                    return render(request, 'college/add_class.html', {'error_message': "Incorrect Syntax!",})
            except:
                return render(request, 'college/add_class.html', {'error_message': "Incorrect Syntax!",})
        else:
            return render(request, 'college/add_class.html', {'error_message': "You didn't enter a class...",})
    return HttpResponseRedirect(reverse('input:add_teacher', args=(name,)))

def save_teacher(request, course_name):
    name = request.POST['teacher-name']
    try:
        #check if course exists
        course = Course.objects.get(course_name=course_name)
        teacher = Choice(course=course, choice_text=name)
        teacher.save()
        return HttpResponseRedirect(reverse('college:index'))
    except Course.DoesNotExist:
        return render(request, 'college/add_teacher.html', {'course_name': course_name, 'error_message': "This class doesn't exist!",})
