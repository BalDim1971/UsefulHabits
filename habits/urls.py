from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitsListView, HabitsCreateView, HabitsDetailView,
                          HabitsUpdateView, HabitsDestroyView)


app_name = HabitsConfig.name

urlpatterns = [
    path('habits/', HabitsListView.as_view(), name='habits_list'),
    path('habits/create/', HabitsCreateView.as_view(), name='habits_create'),
    path('habits/<int:pk>', HabitsDetailView.as_view(), name='habits_detail'),
    path('habits/update/<int:pk>/', HabitsUpdateView.as_view(),
         name='habits_update'),
    path('habits/delete/<int:pk>/', HabitsDestroyView.as_view(),
         name='habits_delete'),
]
