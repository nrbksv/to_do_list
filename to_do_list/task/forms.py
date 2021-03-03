from django.forms import ModelForm, TextInput, Select, Textarea, DateInput


from task.models import Task


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['status', 'task_title', 'full_description', 'deadline']

        widgets = {
            'status': Select(attrs={
                'class': 'form-control'
            }),
            'task_title': TextInput(attrs={
                'class': 'form-control'
            }),
            'full_description': Textarea(attrs={
                'class': 'form-control'
            }),
            'deadline': DateInput(attrs={
                'class': 'form-control'
            })
        }