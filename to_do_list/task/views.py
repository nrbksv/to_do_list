from django.shortcuts import render


def main_view(request):
    return render(request, 'main_page.html')


def add_task(request):
    return render(request, 'add_task.html')
