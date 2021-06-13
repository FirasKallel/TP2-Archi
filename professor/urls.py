from django.urls import path

from professor import views

urlpatterns = [
    path('', views.ProfessorList.as_view(), name=views.ProfessorList.name),
    path('<str:pk>/', views.ProfessorDetail.as_view(), name=views.ProfessorDetail.name),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
