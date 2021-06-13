from django.urls import path

from course.views import CourseRoot
from grade.views import GradeRoot
from professor.views import ProfessorRoot
from promotion.views import PromotionRoot
from student.views import StudentRoot

urlpatterns = [
    path('grade/',
         GradeRoot.as_view(),
         name=GradeRoot.name),
    path('course/',
         CourseRoot.as_view(),
         name=CourseRoot.name),
    path('promotion/',
         PromotionRoot.as_view(),
         name=PromotionRoot.name),
    path('student/',
         StudentRoot.as_view(),
         name=StudentRoot.name),
    path('professor/',
         ProfessorRoot.as_view(),
         name=ProfessorRoot.name),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
