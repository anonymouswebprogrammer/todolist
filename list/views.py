from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.shortcuts import render, get_object_or_404

# Create your views here.
def todo_list(request):
    todos = Todo.objects.filter(deadline_date__lte=timezone.now()).order_by('deadline_date')
    return render(request, 'list/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'list/todo_detail.html', {'todo': todo})
