from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from course.views import CourseList
from grade.views import GradeList
from professor.views import ProfessorList
from promotion.views import PromotionList
from student.views import StudentList


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'Student': reverse(StudentList.name, request=request),
            # 'StudentDetail': reverse(StudentDetail.name, request=request),

            'Professor': reverse(ProfessorList.name, request=request),
            # 'ProfessorDetail': reverse(ProfessorDetail.name, request=request),

            'Promotion': reverse(PromotionList.name, request=request),
            # 'PromotionDetail': reverse(PromotionDetail.name, request=request),

            'Course': reverse(CourseList.name, request=request),
            # 'CourseDetail': reverse(CourseDetail.name, request=request),

            'Grade': reverse(GradeList.name, request=request),
            # 'GradeDetail': reverse(GradeDetail.name, request=request),
        })
