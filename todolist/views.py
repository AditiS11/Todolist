from django.shortcuts import render
from .models import Todolist

# Create your views here.
def index(request):

    todo_item = Todolist.objects.order_by('id') #Creating a variable to hold all the objects from the database that matches and todolist and store it inside the context as a list and furthur use it on our template
    context={'todo_items' : todo_item}
    return render(request,'todolist/index.html',context) #The context is passed to the template where it can be used
