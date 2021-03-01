from django.shortcuts import render, redirect, get_object_or_404


from task.models import Task


def main_view(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'all': 'filter-btn-active'}
    return render(request, 'main_page.html', context)


def add_task_view(request):
    if request.method == 'GET':
        return render(request, 'add_task.html')
    elif request.method == 'POST':
        status = request.POST.get('status')
        task_title = request.POST.get('task_title')
        full_description = request.POST.get('full_description')
        deadline = request.POST.get('deadline')

        if deadline == '':
            deadline = None
        if full_description == '':
            full_description = None

        tasks = Task.objects.create(
            status=status,
            task_title=task_title,
            full_description=full_description,
            deadline=deadline
        )
        return redirect('task-detail', pk=tasks.id)


def detailed_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'task_detail.html', {'task': task})


def filtered_view(request):
    requested_status = request.GET.get('st')
    tasks = Task.objects.filter(status=requested_status)
    context = {
        'tasks': tasks,
        requested_status: 'filter-btn-active'
    }
    return render(request, 'main_page.html', context)


def delete_view(request, pk):
    Task.objects.get(id=pk).delete()
    return redirect('task-list')

