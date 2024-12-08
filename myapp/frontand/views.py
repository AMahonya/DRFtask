from django.shortcuts import render
from rest_framework import generics
from.models import Task
from .serializers import TaskSerializer


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()  # Получаем все задачи
    context = {'tasks': tasks}
    return render(request, 'task_list.html', context)


class TaskAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

