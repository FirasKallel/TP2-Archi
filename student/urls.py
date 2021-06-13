from django.urls import path

from student import views

urlpatterns = [
    path('', views.StudentList.as_view(), name=views.StudentList.name),
    path('<str:pk>/', views.StudentDetail.as_view(), name=views.StudentDetail.name),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
