from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from college.models import Choice, Teacher

def teachers(request):
    choices = Choice.objects.all().values().order_by('-votes')
    return render(request, 'college/teachers.html', {'choices': choices})

def professor(request, name):
    prof = get_object_or_404(Teacher, name=name)
    return render(request, 'college/professor.html', {'prof': prof})

def review(request, name):
    prof = get_object_or_404(Teacher, name=name)
    return render(request, 'college/review.html', {'prof': prof})

def save(request, name):
    prof = get_object_or_404(Teacher, name=name)
    try:
        homework = request.POST['homework']
        difficulty = request.POST['difficulty']
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
        prof.save()
        return HttpResponseRedirect(reverse('teachers:professor', args=(name,)))