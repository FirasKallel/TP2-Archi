from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from student.models import Student
from student.serializers import StudentSerializer


class StudentList(generics.ListCreateAPIView):
    name = 'student-list'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    name = 'student-detail'


class StudentRoot(generics.GenericAPIView):
    name = 'student-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'Student': reverse(StudentList.name, request=request),
        })
