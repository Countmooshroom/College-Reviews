from django.urls import include, path
from . import views

app_name = 'teachers'
urlpatterns = [
    path('', views.teachers, name='teachers'),
]
