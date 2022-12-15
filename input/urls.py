from django.urls import path
from input import views

app_name = 'input'
urlpatterns = [
    path('', views.add_class, name='add_class'),
    path('save-class/', views.save_class, name='save_class'),
    path('teacher/<str:course_name>', views.add_teacher, name='add_teacher'),
    path('save-teacher/<str:course_name>', views.save_teacher, name='save_teacher'),
]