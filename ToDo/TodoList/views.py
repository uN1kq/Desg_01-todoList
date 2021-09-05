from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


from .forms import *
from .models import *


#Views = WebPage (name: Lists)
def lists(request):
    tasks = todo.objects.all()

    form = todoForm()
    if request.method == "POST":
        form = todoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    
    contxt = {'tasks':tasks, 'form':form}
    return render(request, 'TodoList/lists.html', contxt)


#WebPage (name: UpdateList)
def updateList(request, pk):
    tasks = todo.objects.get(id=pk)

    form = todoForm(instance=tasks)
    if request.method == "POST":
        form = todoForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect("/")

    contxt = {'form': form}
    return render(request, 'TodoList/updateList.html', contxt)



def deleteItem(request, pk):
    item = todo.objects.get(id=pk)
    
    if request.method == "POST":
        item.delete()
        return redirect("/")
    
    contxt = { 'item': item }
    return render(request, 'TodoList/deleteItem.html', contxt)


