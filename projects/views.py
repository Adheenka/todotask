from django.shortcuts import render ,redirect
from . models import Task
from . forms import TodoForm
# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        sl_no=request.POST.get('sl_no')
        item_name=request.POST.get('item_name')
        description = request.POST.get('description')
        task = Task(sl_no=sl_no, item_name=item_name,description=description)
        task.save()

    return render(request,'index.html',{'task1':task1})

#def details(request):

 #   return render(request,'detail.html',)
def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
       task.delete()
       return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})