from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . models import todo1
from .forms import todo1form
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.

class tasklist(ListView):
    model = todo1
    template_name ='home.html'
    context_object_name ='out'

class taskdetail(DetailView):
    model = todo1
    template_name = 'detail.html'
    context_object_name = 'out'

class taskupdate(UpdateView):
    model = todo1
    template_name = 'clsupdate.html'
    context_object_name = 'out'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('todo1app:detail',kwargs={'pk':self.object.id})



class taskdelete(DeleteView):
    model = todo1
    template_name = 'delete.html'
    success_url = reverse_lazy('todo1app:list')


def home(request):
    card=todo1.objects.all()
    if request.method =="POST":
        na=request.POST.get('name','')
        pr=request.POST.get('priority','')
        dat=request.POST.get('date','')
        table=todo1(name=na,priority=pr,date=dat)
        table.save()

    return render(request,'home.html',{'card':card})


def delete(request,id):
    dele=todo1.objects.get(id=id)
    if request.method=="POST":
        dele.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    toid=todo1.objects.get(id=id)
    form=todo1form(request.POST or None,instance=toid)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'f':form,'id':toid})

