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

