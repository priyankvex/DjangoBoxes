from datetime import datetime

from django.contrib.auth import authenticate, login
from django.db.models import F
from django.http import HttpResponse
from django_filters import IsoDateTimeFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, Filter
from pytz import utc
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from boxes.models import Box
from boxes.permissions import IsStaffUser
from boxes.serializer import BoxSerializer


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        print("username", username)
        print("password", password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = HttpResponse(status=status.HTTP_200_OK)
        else:
            response = HttpResponse(status=status.HTTP_403_FORBIDDEN)

        return response


class CreateBoxView(CreateAPIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, IsStaffUser)
    serializer_class = BoxSerializer

    def post(self, request, *args, **kwargs):
        request.data["created_by_id"] = request.user.id
        super(CreateBoxView, self).post(request, *args, **kwargs)

        return HttpResponse(status=status.HTTP_201_CREATED)


class UpdateBoxView(UpdateAPIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, IsStaffUser)
    serializer_class = BoxSerializer
    queryset = Box.objects.all()


class BoxListFilter(FilterSet):
    min_length = Filter(field_name="length", lookup_expr="gte")
    max_length = Filter(field_name="length", lookup_expr="lte")
    min_breadth = Filter(field_name="breadth", lookup_expr="gte")
    max_breadth = Filter(field_name="breadth", lookup_expr="lte")
    min_height = Filter(field_name="height", lookup_expr="gte")
    max_height = Filter(field_name="height", lookup_expr="lte")
    min_area = Filter(field_name="area", lookup_expr="gte")
    max_area = Filter(field_name="area", lookup_expr="lte")
    min_volume = Filter(field_name="volume", lookup_expr="gte")
    max_volume = Filter(field_name="volume", lookup_expr="lte")
    created_by = Filter(field_name="created_by_id", lookup_expr="exact")
    min_created_at = IsoDateTimeFilter(field_name='created_at', lookup_expr="gte")
    max_created_at = IsoDateTimeFilter(field_name='created_at', lookup_expr="lte")

    class Meta:
        model = Box
        fields = [
            'min_length', 'max_length', 'min_breadth', 'max_breadth',
            'min_area', 'max_area', 'min_volume', 'max_volume', 'created_by'
        ]


class ListBoxView(ListAPIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('length', 'width', 'height', 'area', 'volume', 'created_at')
    ordering_fields = ('id',)
    filter_class = BoxListFilter
    serializer_class = BoxSerializer

    def get_queryset(self):
        return Box.objects.annotate(
            area=F("length")*F("breadth"),
            volume=F("length")*F("breadth")*F("height")
        )
