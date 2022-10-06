
from django.shortcuts import redirect, render
from .models import TodoListItem
from .forms import TodoListForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_todo_items = TodoListItem.objects.all
            messages.success(request, ('Item has been added to List!'))
            return render(request, 'todolist.html',
                          {'all_items': all_todo_items})
    else:
        all_todo_items = TodoListItem.objects.all
        return render(request, 'todolist.html',
                      {'all_items': all_todo_items})


def delete(request, TodoListItem_id):
    content = TodoListItem.objects.get(pk=TodoListItem_id)
    content.delete()
    messages.success(request, ('Item has been deleted!'))
    return redirect('home')


def cross_off(request, TodoListItem_id):
    content = TodoListItem.objects.get(pk=TodoListItem_id)
    content.completed = True
    content.save()
    return redirect('home')


def uncross(request, TodoListItem_id):
    content = TodoListItem.objects.get(pk=TodoListItem_id)
    content.completed = False
    content.save()
    return redirect('home')


def edit(request, TodoListItem_id):
    if request.method == 'POST':
        content = TodoListItem.objects.get(pk=TodoListItem_id)
        form = TodoListForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited!'))
            return redirect('home')
    else:
        content = TodoListItem.objects.get(pk=TodoListItem_id)
        return render(request, 'edit.html',
                      {'content': content})
