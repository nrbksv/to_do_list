from django.shortcuts import render, redirect, get_object_or_404


from task.models import Task
from task.forms import TaskForm


def main_view(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'all': 'filter-btn-active'}
    return render(request, 'main_page.html', context)


def add_task_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'add_task.html', {'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            tasks = Task.objects.create(
                status=form.cleaned_data.get('status'),
                task_title=form.cleaned_data.get('task_title'),
                full_description=form.cleaned_data.get('full_description'),
                deadline=form.cleaned_data.get('deadline')
            )
            return redirect('task-detail', pk=tasks.id)
        return render(request, 'add_task.html', {'form': form})


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


def delete_confirm_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'GET':
        return render(request, 'delete_confirmation.html', {'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('task-list')


def task_update_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'GET':
        form = TaskForm(initial={
            'status': task.status,
            'task_title': task.task_title,
            'full_description': task.full_description,
            'deadline': task.deadline
        })
        return render(request, 'task_update.html', {'form': form, 'task': task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.status = form.cleaned_data.get('status')
            task.task_title = form.cleaned_data.get('task_title')
            task.full_description = form.cleaned_data.get('full_description')
            task.deadline = form.cleaned_data.get('deadline')
            task.save()
            return redirect('task-detail', pk=task.id)
        return render(request, 'task_update.html', {'form': form, 'task': task})