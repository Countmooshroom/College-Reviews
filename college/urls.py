from django.urls import path
from college import views

app_name = 'college'
urlpatterns = [
    path('', views.index, name='index'),
    path('courses', views.courses, name='courses'),
    path('courses/<str:dept>', views.department, name='department'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.results, name='results'),
    path('<int:course_id>/vote/', views.vote, name='vote'),
]