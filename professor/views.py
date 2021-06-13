from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from professor.models import Professor
from professor.serializers import ProfessorSerializer


class ProfessorList(generics.ListCreateAPIView):
    name = 'professor-list'
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class ProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'professor-detail'
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class ProfessorRoot(generics.GenericAPIView):
    name = 'professor-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'Professor': reverse(ProfessorList.name, request=request),
        })
