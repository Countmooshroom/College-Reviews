from django.shortcuts import render
from college.models import Choice

def teachers(request):
    choices = Choice.objects.all().values().order_by('-votes')
    return render(request, 'college/teachers.html', {'choices': choices})
