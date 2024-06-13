from django.shortcuts import render, redirect
from .models import Todolist
from .forms import TodoListForm

#To allow the post method a decorater needs to be added
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):

    todo_item = Todolist.objects.order_by('id') #Creating a variable to hold all the objects from the database that matches and todolist and store it inside the context as a list and furthur use it on our template
    form=TodoListForm()
    context={'todo_items' : todo_item, 'form': form }
    return render(request,'todolist/index.html',context) #The context is passed to the template where it can be used


@require_POST
def addTodoItem(request):
    form =TodoListForm(request.POST) #Capturing the data entered in the form and storing in a variable
    #To add the form data in to the database
    if form.is_valid():
        new_todo=Todolist(text=request.POST['text'])
        new_todo.save()
    return redirect('index') #Redirecting to the index template


def completedTodo(request,todo_id):
    todo=Todolist.objects.get(pk=todo_id)
    todo.completed=True
    todo.save()
    return redirect('index')
#Takes the request and the unique todo_id to mark that task as completed. It queries the database for that unique todo task and marks it as completed

def deleteCompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()
    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()
    return redirect('index')
