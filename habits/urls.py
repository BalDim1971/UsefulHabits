from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitsListView, HabitsCreateView, HabitsDetailView,
                          HabitsUpdateView, HabitsDestroyView, PublicHabitListView)


app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitsListView.as_view(), name='habits_list'),
    path('public/', PublicHabitListView.as_view(), name="habits_public_list"),
    path('create/', HabitsCreateView.as_view(), name='habits_create'),
    path('<int:pk>', HabitsDetailView.as_view(), name='habits_detail'),
    path('update/<int:pk>/', HabitsUpdateView.as_view(),
         name='habits_update'),
    path('delete/<int:pk>/', HabitsDestroyView.as_view(),
         name='habits_delete'),
]
