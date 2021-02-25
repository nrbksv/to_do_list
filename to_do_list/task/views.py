from django.shortcuts import render

from task.models import Task


def main_view(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'status_ru': Task.STATUS_CHOICES, 'all': 'active'}
    return render(request, 'main_page.html', context)


def add_task_view(request):
    if request.method == 'GET':
        return render(request, 'add_task.html', {'status': Task.STATUS_CHOICES})
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
        context = {'tasks': tasks, 'status_ru': Task.STATUS_CHOICES, 'all': 'active'}
        return render(request, 'main_page.html', context)


def filtered_view(request):
    requested_status = request.GET.get('st')
    tasks = Task.objects.filter(status=requested_status)
    context = {
        'tasks': tasks,
        requested_status: 'active',
        'status_ru': Task.STATUS_CHOICES,
    }
    return render(request, 'main_page.html', context)


def delete_view(request):
    del_id = request.GET.get('id')
    Task.objects.get(id=del_id).delete()
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'status_ru': Task.STATUS_CHOICES, 'all': 'active'}
    return render(request, 'main_page.html', context)

