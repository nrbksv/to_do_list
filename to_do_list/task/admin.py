from django.contrib import admin

from task.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'deadline']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['status', 'description', 'deadline']


admin.site.register(Task, TaskAdmin)

