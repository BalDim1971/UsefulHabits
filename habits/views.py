"""
Вьюшки Generic-классы для модели Привычка
"""

from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.serializers import HabitsSerializer, HabitsListSerializer
from users.permissions import IsOwner


class HabitsListView(generics.ListAPIView):
    serializer_class = HabitsListSerializer
    queryset = Habits.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'owner']
    ordering_fields = ['name', 'owner']
    # filterset_fields = ['owner']


class HabitsCreateView(generics.CreateAPIView):
    serializer_class = HabitsSerializer


class HabitsDetailView(generics.RetrieveAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()


class HabitsDestroyView(generics.DestroyAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsUpdateView(generics.UpdateAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
