import json
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from todo.forms import CreateListForm, CreateTaskForm
from todo.models import List, Task



def index(request):
    lists_all = List.objects.all()
    if request.method == "POST":
        form = CreateListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CreateListForm()
    return render(request,  "cards/to_do_card.html", {"form": form,"title": "To Do","items": lists_all })
    # context = {
    #     "title": "To Do",
    #     "items": lists_all
    # }
    # return render(request, "cards/to_do_card.html" , context)

def hero(request):
    context = {
        "title": "To Do",
    }
    return render(request, "heroes/hero.html")

def main(request):
    context = {
        "title": "To Do",
    }
    return render(request, "main.html")

def create_list_form(request):
    # mount = get_object_or_404(List, list_id=mount_id)
    if request.method == "POST":
        form = CreateListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CreateListForm()
    return render(request, "forms/create_list_form.html", {"form": form,"title" : "Create List" })

def tasks(request,list_num):
    #selected list
    list = List.objects.get(id=list_num)
    #tasks for list
    related_tasks = list.tasks.all()
    completed_tasks = related_tasks.filter(status=True).count()
    total_tasks = related_tasks.count()
    context = {
        "title": list.list_name,
        "tasks": related_tasks,
        "total":total_tasks,
        "completed": completed_tasks,
        "list_id" : list_num
    }
    return render(request, "cards/to_do_tasks.html" , context)

def new_tasks(request,list_num):
    #selected list
    # list = List.objects.get(id=list_num)
    #tasks for list
    
    list = get_object_or_404(List, pk=list_num)
    related_tasks = list.tasks.all()
    completed_tasks = related_tasks.filter(status=True).count()
    total_tasks = related_tasks.count()
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.list = list
            new_task.save()
            return redirect("tasks", list_num=list_num)
    else:
        form = CreateTaskForm()
        context = {
    "title": list.list_name,
    "tasks": related_tasks,
    "form" : form,
    "list_id" : list_num,
    "total":total_tasks,
    "completed": completed_tasks,
}
    return render(request, "forms/create_tasks_form.html" , context)

@csrf_exempt
def update_task_status(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=task_id)
        task.status = not task.status  # Toggle status
        task.save()
        return redirect('tasks',task.list.pk)
    return redirect('tasks',task.list.pk)

@csrf_exempt
def update_task_name(request, task_id , updated_name):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=task_id)
        task.task_name = updated_name  # Toggle status
        task.save()
        return redirect('tasks', task.list.pk)
    return redirect('tasks', task.list.pk)

@csrf_exempt
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "partials/edit_task_name.html", {"task": task,"task_name":"new name"})

# @csrf_exempt
def save_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        # task.task_name = request.POST.get("newTaskName", task.task_name)
        data = json.loads(request.body)
        task_name = data.get("newTaskName")
        task.task_name = task_name
        task.save()
        return JsonResponse({'status': 'success', 'message': 'Task saved!'})
    return redirect('tasks', task.list.pk)

@csrf_exempt
def cancel_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return redirect('tasks', task.list.pk)

# @csrf_exempt
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete() # Toggle status
    return redirect('tasks',task.list.pk)
    # return new_tasks(request,task.list.pk)
    # return render(request, "forms/create_tasks_form.html")
    # return render(request, "forms/create_tasks_form.html")



# def update_task_status(request, task_id):
#     task = get_object_or_404(Task, pk=task_id)
    
    
    
#     if request.method == "POST":
#         task.status = not task.status  # Toggle status
#         task.save()
#         related_list = task.list
#         related_tasks = related_list.tasks.all()
#         completed_tasks = related_tasks.filter(status=True).count()
#         total_tasks = related_tasks.count()
#         context = {
#     "title": task.list.list_name,
#     "tasks": related_tasks,
#     "list_id" : related_list.pk,
#     "total":total_tasks,
#     "completed": completed_tasks,
# }
#     return render(request, "forms/create_tasks_form.html" , context)