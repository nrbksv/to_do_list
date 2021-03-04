"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task.views import (
    main_view, add_task_view, filtered_view,
    detail_view, task_update_view, delete_view
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='task-list'),
    path('task/<int:pk>', detail_view, name='task-detail'),
    path('task/add/', add_task_view, name='task-add'),
    path('task/status/', filtered_view, name='task-filter'),
    path('task/<int:pk>/update', task_update_view, name='task-update'),
    path('task/<int:pk>/delete/confirm', delete_view, name='delete-confirm')
]
