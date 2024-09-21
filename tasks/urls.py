from django.urls import path
from .views import index, update_task, remove_task, complete_task

urlpatterns = [
    path('', index, name="list"),
    path('update_task/<str:primary_key>/', update_task),
    path('remove_task/<str:primary_key>/', remove_task),
    path('complete_task/<str:primary_key>/', complete_task),
]
