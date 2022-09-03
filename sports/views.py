from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from sports.models import Sport
from sports.serializer import SportSerializer


class SportAPIView(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin):
    serializer_class = SportSerializer
    queryset = Sport.objects.all()