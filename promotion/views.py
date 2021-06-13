from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from promotion.models import Promotion
from promotion.serializers import PromotionSerializer


class PromotionList(generics.ListCreateAPIView):
    name = 'promotion-list'
    # queryset = Promotion.objects.values('id', 'graduation_year').prefetch_related('students').all()
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class PromotionDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'promotion-detail'
    queryset = Promotion.objects.values('id', 'graduation_year', 'students').all()
    serializer_class = PromotionSerializer


class PromotionRoot(generics.GenericAPIView):
    name = 'promotion-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'Promotion': reverse(PromotionList.name, request=request),
        })
