from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from college.models import Choice, Teacher

def teachers(request):
    choices = Choice.objects.all().values().order_by('-votes')
    teacher_list = []
    for choice in choices:
        teacher_list.append(choice['choice_text'])
    #remove duplicates
    teacher_list = list(dict.fromkeys(teacher_list))
    return render(request, 'college/teachers.html', {'choices': choices, 'teacher_list': teacher_list})

def professor(request, name):
    try:
        prof = Teacher.objects.get(name=name)
    except Teacher.DoesNotExist:
        #get a list of known teachers
        choices = Choice.objects.all().values().order_by('-votes')
        teacher_list = []
        for choice in choices:
            teacher_list.append(choice['choice_text'])
        #create a new object for the professor
        if name in teacher_list:
            prof = Teacher(name=name)
            prof.save()
    return render(request, 'college/professor.html', {'prof': prof})

def review(request, name):
    try:
        prof = Teacher.objects.get(name=name)
    except Teacher.DoesNotExist:
        prof = Teacher(name=name)
        prof.save()
    return render(request, 'college/review.html', {'prof': prof})

def save(request, name):
    prof = get_object_or_404(Teacher, name=name)
    try:
        homework = request.POST['homework']
        difficulty = request.POST['difficulty']
        essays = request.POST['essays']
        attendance = request.POST['attendance']
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'college/review.html', {
            'prof': prof,
            'error_message': "You didn't select a choice.",
        })
    else:
        prof.homework_sum += int(homework)
        prof.homework_count += 1
        prof.difficulty_sum += int(difficulty)
        prof.difficulty_count += 1
        prof.essays_sum += int(essays)
        prof.essays_count += 1
        prof.attendance_sum += int(attendance)
        prof.attendance_count += 1
        prof.save()
        return HttpResponseRedirect(reverse('teachers:professor', args=(name,)))