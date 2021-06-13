from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from course.models import Course
from course.serializers import CourseSerializer


class CourseList(generics.ListCreateAPIView):
    name = 'course-list'
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'course-detail'
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRoot(generics.GenericAPIView):
    name = 'course-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'Course': reverse(CourseList.name, request=request),
        })
