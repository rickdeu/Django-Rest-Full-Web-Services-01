from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from drones.models import *
from drones.serializers import *
from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter


class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-list'

    filter_fields = (
        'name',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
    )


class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-detail'


class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'
    filter_fields = (
        'name',
        'drone_category',
        'manufacturing_date',
        'has_it_competed',
    )
    search_fields = (
        '^name',

    )
    ordering_fields = (
        'name',
        'manufacturing_date',

    )


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'


class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-list'
    filter_fields = (
        'name',
        'gender',
        'races_count',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
        'races_count'
    )


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'


class CompetitionFilter(filters.BaseFilterBackend):
    # CompetitionFilter(filters.FilterSet):
    from_achievement_date = DateTimeFilter(name='distance_achievement_date', lookup_expr='gte')
    to_achievement_date = DateTimeFilter(name='distance_achievement_date', lookup_expr='lte')
    min_distance_in_feet = NumberFilter(name='distance_in_feet', lookup_expr='gte')
    max_distance_in_feet = NumberFilter(name='distance_in_feet', lookup_expr='lte')
    drone_name = AllValuesFilter(name='drone__name',)
    pilot_name = AllValuesFilter(name='pilot__name',)

    class Meta:
        model = Competition
        fields = (
            'distance_in_feet',
            'from_achievement_date',
            'to_achievement_date',
            'min_distance_in_feet',
            'max_distance_in_feet',
            # drone__name will be accessed as drone_name
            'drone_name',
            # pilot__name will be accessed as pilot_name
            'pilot_name',
        )


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-list'

    filter_class = CompetitionFilter
    ordering_fields = (
        'distance_in_feet',
        'distance_achievement_date',
        )


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request,  *args, **kwargs):
        return Response(
            {
                'drone-categories': reverse(DroneCategoryList.name, request=request),
                'drones': reverse(DroneList.name, request=request),
                'pilots': reverse(PilotList.name, request=request),
                'competitions': reverse(CompetitionList.name, request=request)
            }
        )
