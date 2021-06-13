from django.urls import path

from course import views

urlpatterns = [
    path('', views.CourseList.as_view(), name=views.CourseList.name),
    path('<int:pk>/', views.CourseDetail.as_view(), name=views.CourseDetail.name),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
