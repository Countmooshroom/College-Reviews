from django.urls import include, path
from . import views

app_name = 'teachers'
urlpatterns = [
    path('', views.teachers, name='teachers'),
    path('<str:name>/', views.professor, name='professor'),
    path('<str:name>/review', views.review, name='review'),
    path('<str:name>/save', views.save, name='save'),
]
