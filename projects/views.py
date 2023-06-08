from django.shortcuts import render ,redirect,get_object_or_404
from . models import Task

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


def update(request, taskid):
    task = Task.objects.get(id=taskid)

    if request.method == 'POST':
        sl_no = request.POST.get('sl_no')
        item_name = request.POST.get('item_name')
        description = request.POST.get('description')
        
        task.sl_no = sl_no
        task.item_name = item_name
        task.description = description
        task.save()
        return redirect('/')
    return render(request, 'edit.html', {'task': task})