"""
Вьюшки Generic-классы для модели Привычка
"""

from rest_framework import generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from habits.models import Habits
from habits.pagination import HabitsPagination
from habits.serializers import HabitsSerializer, HabitsListSerializer
from users.permissions import IsOwner


class HabitsListView(generics.ListAPIView):
    serializer_class = HabitsListSerializer
    queryset = Habits.objects.all().order_by('id')
    pagination_class = HabitsPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'owner']
    ordering_fields = ['name', 'owner']
    permission_classes = [IsAuthenticated, IsOwner]
    # filterset_fields = ['owner']

    def get_queryset(self):
        return Habits.objects.filter(owner=self.request.user).order_by('id')


class HabitsCreateView(generics.CreateAPIView):
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitsDetailView(generics.RetrieveAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsDestroyView(generics.DestroyAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if len(Habits.objects.filter(associated_habits=instance)) > 0:
            return Response({'error_message': 'Это связанная привычка,'
                                              ' не могу удалить'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class HabitsUpdateView(generics.UpdateAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitListView(generics.ListAPIView):
    """Контроллер списка публичных привычек"""
    queryset = Habits.objects.filter(is_public=True).order_by('pk')
    serializer_class = HabitsSerializer
    pagination_class = HabitsPagination
