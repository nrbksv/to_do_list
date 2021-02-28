from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]

    status = models.CharField(max_length=20, default='new', blank=True)
    task_title = models.CharField(max_length=200, null=False, blank=False)
    full_description = models.TextField(max_length=2000, null=True, blank=True)
    deadline = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.status} {self.task_title} {self.full_description} {self.deadline}'
