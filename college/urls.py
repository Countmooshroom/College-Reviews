from django.urls import path
from college import views

app_name = 'college'
urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('courses/<str:dept>', views.department, name='department'),
    path('courses/<str:dept>/<str:name>/', views.course, name='course'),
    path('courses/<str:dept>/<str:name>/vote/', views.vote, name='vote'),
    path('courses/<str:dept>/<str:name>/save/', views.save, name='save'),
]