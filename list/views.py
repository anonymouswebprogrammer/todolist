from django.shortcuts import render

# Create your views here.
def todo_list(request):
    return render(request, 'list/todo_list.html')
