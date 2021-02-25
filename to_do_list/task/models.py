from django.db import models


class Task(models.Model):
    status = models.CharField(max_length=20, default='new', blank=True)
    description = models.TextField(max_length=1000, null=False, blank=False)
    deadline = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.status} {self.deadline} {self.description}'
