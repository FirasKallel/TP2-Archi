import json

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from grade.models import Grade
from grade.serializers import GradeSerializer


class GradeList(generics.ListCreateAPIView):
    name = 'grade-list'
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class GradeDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'course-detail'
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class GradeRoot(generics.GenericAPIView):
    name = 'grade-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'Grade': reverse(GradeList.name, request=request),
        })
