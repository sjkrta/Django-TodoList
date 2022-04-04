from django.shortcuts import redirect, render
from .models import Todo

# Create your views here.
def index(request):
    if request.method =='POST':
        todo =request.POST['todo']
        print(todo)
        Todo.objects.create(todo = request.POST['todo'])
    return render(request, 'index.html', context={
        "Todo": Todo.objects.all()
    })

def delete(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('home')