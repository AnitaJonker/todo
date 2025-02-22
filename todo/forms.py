from django import forms
from django.forms.widgets import (
    MultiWidget,
    TextInput,
    Widget,
    NumberInput,
    Input,
)
from .models import List, Task, Tag

class CreateListForm(forms.ModelForm):
    reflectometer_name = forms.TextInput()

    class Meta:
        model = List
        fields = ["list_name"]
        # exclude = ["reflectometer_id"]

    def __init__(self, *args, **kwargs):
        super(CreateListForm, self).__init__(*args, **kwargs)
        
class CreateTaskForm(forms.ModelForm):
    reflectometer_name = forms.TextInput()

    class Meta:
        model = Task
        fields = ["task_name"]
        # exclude = ["reflectometer_id"]

    def __init__(self, *args, **kwargs):
        super(CreateTaskForm, self).__init__(*args, **kwargs)
