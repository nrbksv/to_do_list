from django.shortcuts import render
from task.models import Task


def main_view(request):
    tasks = Task.objects.all()
    return render(request, 'main_page.html', context={'tasks': tasks})


def add_task_view(request):
    if request.method == 'GET':
        return render(request, 'add_task.html')
    elif request.method == 'POST':
        status = request.POST.get('status')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')

        if deadline == '':
            deadline = None

        Task.objects.create(
            status=status,
            description=description,
            deadline=deadline
        )
        tasks = Task.objects.all()
        return render(request, 'main_page.html', context={'tasks': tasks})
